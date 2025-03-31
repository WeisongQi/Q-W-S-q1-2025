const express = require('express');
const cors = require('cors');
const fs = require('fs').promises; // 使用异步文件操作
const app = express();
const port = 5050;

// ================= 中间件配置 =================
app.use(cors()); // 启用 CORS 支持
app.use(express.json()); // 解析 JSON 请求体
app.use(cors({
    origin: ["http://localhost:5500", "null"]
}))

// ================= 通用工具函数 =================


const readData = async () => {
    try {
        const data = await fs.readFile('produkteList.json', 'utf8');
        return JSON.parse(data);
    } catch (error) {
        if (error.code === 'ENOENT') {
            // 如果文件不存在，创建空数组
            await writeData([]);
            return [];
        }
        throw error;
    }
};

const writeData = async (data) => {
    await fs.writeFile('produkteList.json', JSON.stringify(data, null, 2));
};

const generateId = () => {
    return Math.floor(100000 + Math.random() * 900000);
};

// ================= 错误处理中间件 =================
app.use((err, req, res, next) => {
    console.error('[Server Error]', err);
    res.status(500).json({
        error: 'Internal Server Error',
        message: err.message
    });
});

// ================= 路由定义 =================

// GET /produkte - 获取所有产品
app.get("/produkte", async (req, res, next) => {
    try {
        const products = await readData();
        res.json(products);
    } catch (error) {
        next(error);
    }
});

// GET /produkte/search - 搜索产品
app.get("/produkte/search", async (req, res, next) => {
    try {
        const { sorten, name, art } = req.query;
        const products = await readData();

        const filtered = products.filter(p =>
            (!sorten || p.sorten === sorten) &&
            (!name || p.name === name) &&
            (!art || p.art === art)
        );

        res.json(filtered);
    } catch (error) {
        next(error);
    }
});

// POST /produkte - 创建新产品
app.post("/produkte", async (req, res, next) => {
    try {
        const { name, sorten, art } = req.body;

        // 验证必填字段
        if (!name || !sorten || !art) {
            return res.status(400).json({
                error: "Validation Error",
                message: "缺少必填字段: name, sorten, art"
            });
        }

        const products = await readData();
        const newProduct = {
            id: generateId(), // 生成唯一 ID
            name,
            sorten,
            art
        };

        products.push(newProduct);
        await writeData(products);

        res.status(201).json(newProduct);
    } catch (error) {
        next(error);
    }
});

// PUT /produkte/:id - 更新产品
app.put("/produkte/:id", async (req, res, next) => {
    try {
        const products = await readData();
        const productId = req.params.id;
        const { name, sorten, art } = req.body;

        // 查找产品索引
        const index = products.findIndex(p => p.id == productId);
        if (index === -1) {
            return res.status(404).json({
                error: "Not Found",
                message: "指定 ID 的产品不存在"
            });
        }

        // 更新字段（保留未提供的原始值）
        const updatedProduct = {
            ...products[index],
            name: name || products[index].name,
            sorten: sorten || products[index].sorten,
            art: art || products[index].art
        };

        products[index] = updatedProduct;
        await writeData(products);

        res.json(updatedProduct);
    } catch (error) {
        next(error);
    }
});

// DELETE /produkte/:id - 删除产品
app.delete("/produkte/:id", async (req, res, next) => {
    try {
        const productId = req.params.id;
        const products = await readData();

        // 验证 ID 有效性
        if (!productId) {
            return res.status(400).json({
                error: "Invalid Request",
                message: "必须提供产品 ID"
            });
        }

        const index = products.findIndex(p => p.id == productId);
        if (index === -1) {
            return res.status(404).json({
                error: "Not Found",
                message: "指定 ID 的产品不存在"
            });
        }

        const [deletedProduct] = products.splice(index, 1);
        await writeData(products);

        res.json({
            message: "删除成功",
            deletedProduct
        });
    } catch (error) {
        next(error);
    }
});

// ================= 启动服务器 =================
app.listen(port, () => {
    console.log(`服务器运行中: http://localhost:${port}`);
});
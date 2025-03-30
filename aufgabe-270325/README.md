# Aufgabe 270325

## Beschreibung (Deutsch)

Dieses Projekt ist eine einfache REST-API, die mit Express.js erstellt wurde. Sie ermöglicht das Verwalten einer Liste von Büchern. Die API bietet Endpunkte zum Abrufen, Suchen, Hinzufügen und Anzeigen von Büchern.

---

### Wichtige Hinweise

- **Reihenfolge der Routen**:
  Beim Programmieren der API ist es wichtig, dass die Route `/books/search` vor der Route `/books/:id` definiert wird. Andernfalls wird die `/books/search`-Route nicht funktionieren, da die `/books/:id`-Route alle Anfragen mit einem Parameter nach `/books/` abfängt.

---
### Installation

1. Stellen Sie sicher, dass Node.js und npm auf Ihrem System installiert sind.
2. Klonen Sie das Repository und navigieren Sie in das Projektverzeichnis:
   ```bash
   git clone <repository-url>
   cd aufgabe-270325
   ```
3. Installieren Sie die Abhängigkeiten:
   ```bash
   npm install
   ```

---

### Nutzung

1. Starten Sie den Server:
   ```bash
   npm start
   ```
2. Die API ist unter `http://localhost:5400` verfügbar.

---

### API-Endpunkte

1. **Abrufen aller Bücher**
   - **GET** `/books`
   - Antwort: Eine Liste aller Bücher.

2. **Suchen eines Buches nach Titel**
   - **GET** `/books/search?title=<Titel>`
   - Parameter: `title` - Der Titel des Buches.
   - Antwort: Das gefundene Buch oder ein Fehler, wenn kein Buch gefunden wurde.

3. **Abrufen eines Buches nach ID**
   - **GET** `/books/:id`
   - Parameter: `id` - Die ID des Buches.
   - Antwort: Das Buch mit der angegebenen ID oder ein Fehler, wenn kein Buch gefunden wurde.

4. **Hinzufügen eines neuen Buches**
   - **POST** `/books`
   - Body (JSON):

     ```json

     {
       "title": "Buchtitel",
       "author": "Autorname"
     }
     ```
   - Antwort: Die aktualisierte Liste aller Bücher.

---

### Daten

Die Bücherliste wird in der Datei `jsonDateBooks/bookOutput.json` gespeichert.

---

### Abhängigkeiten

- **express**: Web-Framework für Node.js
- **nodemon**: Entwicklungswerkzeug für automatisches Neustarten des Servers
- **fs**: Modul für Dateisystemoperationen

---

### Lizenz

Dieses Projekt ist unter der ISC-Lizenz veröffentlicht.

---

## 描述 (中文)

本项目是一个使用 Express.js 构建的简单 REST API，用于管理书籍列表。API 提供了获取、搜索、添加和查看书籍的端点。

---

### 安装

1. 确保您的系统已安装 Node.js 和 npm。
2. 克隆此仓库并进入项目目录：
   ```bash
   git clone <repository-url>
   cd aufgabe-270325
   ```
3. 安装依赖：
   ```bash
   npm install
   ```

---

### 使用

1. 启动服务器：
   ```bash
   npm start
   ```
2. API 可通过 `http://localhost:5400` 访问。

---

### API 端点

1. **获取所有书籍**
   - **GET** `/books`
   - 返回：所有书籍的列表。

2. **根据标题搜索书籍**
   - **GET** `/books/search?title=<标题>`
   - 参数：`title` - 书籍标题。
   - 返回：找到的书籍或未找到书籍的错误。

3. **根据 ID 获取书籍**
   - **GET** `/books/:id`
   - 参数：`id` - 书籍 ID。
   - 返回：具有指定 ID 的书籍或未找到书籍的错误。

4. **添加新书籍**
   - **POST** `/books`
   - 请求体 (JSON)：
     ```json
     {
       "title": "书名",
       "author": "作者"
     }
     ```
   - 返回：更新后的所有书籍列表。

---

### 重要提示

- **路由顺序**: 在编程时，必须确保 `/books/search` 路由定义在 `/books/:id` 路由之前。否则，`/books/search` 功能将无法正常工作，因为 `/books/:id` 路由会拦截所有带参数的 `/books/` 请求。

---

### 数据

书籍列表保存在文件 `jsonDateBooks/bookOutput.json` 中。

---

### 依赖项

- **express**: Node.js 的 Web 框架
- **nodemon**: 用于自动重启服务器的开发工具
- **fs**: 文件系统操作模块

---

### 许可证

本项目使用 ISC 许可证发布。

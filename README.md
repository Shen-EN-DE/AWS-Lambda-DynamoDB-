---

# 寶可夢API

這個項目使用AWS服務，包括Amplify、API Gateway、Lambda和DynamoDB來創建一個寶可夢API。這個API允許用戶查看所有寶可夢信息並進行捕捉。

## 系統架構

此API使用以下AWS服務：

- **Amplify**：用於部署和管理前端應用。
- **API Gateway**：提供一個RESTful API，用於處理前端請求。
- **Lambda**：處理API請求的邏輯，包括從DynamoDB檢索數據。
- **DynamoDB**：存儲所有寶可夢數據。

## 功能流程

1. **用戶** 透過前端界面向Amplify發送請求，要求獲取所有寶可夢。
2. Amplify通過API Gateway轉發這些請求。
3. API Gateway觸發Lambda函數，該函數從DynamoDB獲取數據。
4. 數據返回給Lambda函數，然後透過API Gateway返回給Amplify。
5. Amplify將寶可夢數據展示給用戶。

## 使用說明

- 訪問部署後的網站，查看和捕捉寶可夢。
- 輸入寶可夢名稱進行捕捉，並查看詳細信息。

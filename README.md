# AI Agent 简历诊断

一个基于 Streamlit 的简历诊断小工具

## 功能

- 输出目标岗位
- 粘贴简历文本
- 根据关键词进行评分
- 输出针对性的优化建议

## 项目亮点

- 使用 Streamlit 构建交互式 Web 页面
- 接入兼容 OpenAI SDK 的大模型 API
- 支持根据目标岗位进行简历诊断
- 对 API Key 缺失和调用失败进行异常处理
- 输出评分、核心问题和修改建议，便于用户快速优化简历

## 简历写法

AI 简历诊断 Agent｜Python / Streamlit / LLM API

- 基于 Streamlit 构建交互式简历诊断页面，支持目标岗位输入和简历文本分析
- 接入兼容 OpenAI SDK 的大模型 API，实现简历评分、核心问题识别和修改建议生成
- 设计 API Key 缺失检测与异常处理逻辑，提升应用稳定性和可用性

## 运行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```
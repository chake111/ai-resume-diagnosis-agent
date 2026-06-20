import streamlit as st
import os
from openai import OpenAI
from database import init_db


init_db()
api_key = os.getenv("DEEPSEEK_API_KEY")


def diagnose_resume(resume_content, target_post):
    if not api_key:
        return "未检测到 DEEPSEEK_API_KEY，请先配置环境变量。"
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    prompt = f"""
    你是诊断简历 Agent。
    目标岗位: {target_post}
    
    请诊断下面的简历，输出：
    1.简历评分（0-100）
    2.3条最重要的修改简历
    
    简历内容：
    {resume_content}
    
    请严格按以下格式输出：

    ## 简历评分
    分数：X/100
    
    ## 核心问题
    1. ...
    2. ...
    3. ...
    
    ## 修改建议
    1. ...
    2. ...
    3. ...
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    except Exception as e:
        return f"AI Api 调用失败：{e}"
    return response.choices[0].message.content



st.title("AI 简历诊断 Agent")

st.set_page_config(
    page_title = "AI 简历诊断 Agent",
    page_icon = "📄",
    layout = "centered",
)

st.caption("快速针对优化JD给出优化方案")
st.divider()

sample_resume = ""

if os.path.exists("sample_resume.txt"):
    with open("sample_resume.txt", "r", encoding="utf-8") as file:
        sample_resume = file.read()


target_role = st.text_input("目标岗位", value="AI Agent 开发实习生")

if "resume_input" not in st.session_state:
    st.session_state.resume_input = sample_resume

if st.button("清空"):
    st.session_state.resume_input = ""

resume_text = st.text_area("粘贴你的简历内容",key = "resume_input", height=300)

if st.button("开始诊断"):
    if not resume_text.strip():
        st.warning("请先粘贴简历内容")
    else:
        st.subheader("诊断结果")
        with st.spinner("AI 正在诊断简历..."):
            result = diagnose_resume(resume_text, target_role)
        st.write(result)

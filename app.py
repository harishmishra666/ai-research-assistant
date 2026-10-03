import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import os
import re

from utils.research import search_web


# =====================================================
# ENVIRONMENT
# =====================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:

    st.error(
        "GEMINI_API_KEY not found. "
        "Please check your .env file."
    )

    st.stop()


client = genai.Client(
    api_key=GEMINI_API_KEY
)


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)


# =====================================================
# SESSION STATE
# =====================================================

if "web_results" not in st.session_state:

    st.session_state.web_results = []


if "web_query" not in st.session_state:

    st.session_state.web_query = ""


if "ai_summary" not in st.session_state:

    st.session_state.ai_summary = ""


if "research_report" not in st.session_state:

    st.session_state.research_report = ""


if "pdf_text" not in st.session_state:

    st.session_state.pdf_text = ""


if "pdf_analysis" not in st.session_state:

    st.session_state.pdf_analysis = ""


# =====================================================
# PROFESSIONAL PDF GENERATOR
# =====================================================

def create_research_pdf(
    title,
    topic,
    content,
    sources
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]

    title_style.alignment = TA_CENTER

    story = []

    # -------------------------------------------------
    # COVER / TITLE
    # -------------------------------------------------

    story.append(
        Spacer(1, 100)
    )

    story.append(
        Paragraph(
            "🔬 AI RESEARCH ASSISTANT",
            title_style
        )
    )

    story.append(
        Spacer(1, 25)
    )

    story.append(
        Paragraph(
            f"<b>{title}</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            f"<b>Research Topic:</b> {topic}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "AI-generated research report based on "
            "web research sources.",
            styles["BodyText"]
        )
    )

    story.append(
        PageBreak()
    )

    # -------------------------------------------------
    # AI SUMMARY CONTENT
    # -------------------------------------------------

    for line in content.split("\n"):

        line = line.strip()

        if not line:

            story.append(
                Spacer(1, 8)
            )

            continue


        # Remove markdown bold markers
        clean_line = line.replace(
            "**",
            ""
        )


        # Main heading
        if clean_line.startswith("# "):

            heading = clean_line[2:]

            story.append(
                Paragraph(
                    heading,
                    styles["Heading1"]
                )
            )


        # Secondary heading
        elif clean_line.startswith("## "):

            heading = clean_line[3:]

            story.append(
                Paragraph(
                    heading,
                    styles["Heading2"]
                )
            )


        # Third heading
        elif clean_line.startswith("### "):

            heading = clean_line[4:]

            story.append(
                Paragraph(
                    heading,
                    styles["Heading3"]
                )
            )


        # Bullet
        elif clean_line.startswith("- "):

            bullet = clean_line[2:]

            story.append(
                Paragraph(
                    f"• {bullet}",
                    styles["BodyText"]
                )
            )


        # Numbered list
        elif re.match(
            r"^\d+\.",
            clean_line
        ):

            story.append(
                Paragraph(
                    clean_line,
                    styles["BodyText"]
                )
            )


        # Normal paragraph
        else:

            # Escape basic HTML characters
            clean_line = (
                clean_line
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            story.append(
                Paragraph(
                    clean_line,
                    styles["BodyText"]
                )
            )


        story.append(
            Spacer(1, 5)
        )


    # -------------------------------------------------
    # REFERENCES
    # -------------------------------------------------

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "References",
            styles["Heading1"]
        )
    )

    story.append(
        Spacer(1, 10)
    )


    for i, source in enumerate(
        sources,
        start=1
    ):

        source_title = source.get(
            "title",
            "Untitled Source"
        )

        source_url = source.get(
            "url",
            ""
        )

        story.append(
            Paragraph(
                f"<b>{i}. {source_title}</b>",
                styles["BodyText"]
            )
        )

        if source_url:

            story.append(
                Paragraph(
                    source_url,
                    styles["BodyText"]
                )
            )

        story.append(
            Spacer(1, 8)
        )


    # -------------------------------------------------
    # BUILD PDF
    # -------------------------------------------------

    doc.build(
        story
    )

    buffer.seek(0)

    return buffer


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    selected = option_menu(

        "🔬 AI Research Assistant",

        [
            "🏠 Home",
            "🔬 Research",
            "🌐 Web Research",
            "📄 PDF Analyzer",
            "💬 Ask AI"
        ],

        icons=[
            "house",
            "search",
            "globe",
            "file-earmark-pdf",
            "chat-dots"
        ],

        menu_icon="🔬",

        default_index=0
    )


# =====================================================
# HOME
# =====================================================

if selected == "🏠 Home":

    st.title(
        "🔬 AI Research Assistant"
    )

    st.subheader(
        "Your intelligent research companion"
    )

    st.write(
        "AI-powered research companion for "
        "students, researchers and educators."
    )

    st.divider()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            """
            ### 🔬 Research

            Generate structured AI-powered
            research reports from a topic.
            """
        )


    with col2:

        st.markdown(
            """
            ### 🌐 Web Research

            Search the web and discover
            useful research sources.
            """
        )


    with col3:

        st.markdown(
            """
            ### 📄 PDF Analyzer

            Upload research papers and
            analyze them using AI.
            """
        )


    st.divider()


    st.subheader(
        "✨ Key Features"
    )


    st.markdown(
        """
        - 🤖 Gemini AI research generation
        - 🌐 Web source discovery
        - 🔗 Clickable research sources
        - 📄 PDF research paper analysis
        - 💬 Ask questions from PDFs
        - 📥 Download research reports
        - 🧠 AI-powered research insights
        - 📚 Automatic references
        """
    )


# =====================================================
# RESEARCH
# =====================================================

elif selected == "🔬 Research":

    st.title(
        "🔬 AI Research Generator"
    )

    st.write(
        "Enter a research topic and generate "
        "a structured research report."
    )

    st.divider()


    research_topic = st.text_input(
        "Enter Research Topic",
        placeholder=(
            "Example: Artificial Intelligence "
            "in Education"
        )
    )


    if st.button(
        "🤖 Generate Research Report"
    ):

        if not research_topic:

            st.warning(
                "Please enter a research topic."
            )

        else:

            with st.spinner(
                "🤖 Generating research report..."
            ):

                try:

                    prompt = f"""
You are an AI research assistant.

Generate a structured research report on:

{research_topic}

Include:

1. Introduction
2. Research Overview
3. Research Questions
4. Key Findings
5. Applications
6. Challenges
7. Research Gaps
8. Future Scope
9. Conclusion

Use clear professional academic language.
"""

                    response = client.models.generate_content(

                        model="gemini-2.5-flash",

                        contents=prompt
                    )


                    research_report = response.text


                    st.session_state.research_report = (
                        research_report
                    )


                    st.success(
                        "Research report generated!"
                    )


                    st.markdown(
                        research_report
                    )


                    st.download_button(

                        "📥 Download TXT",

                        research_report,

                        file_name=(
                            "research_report.txt"
                        ),

                        mime="text/plain"
                    )


                except Exception as e:

                    st.error(
                        f"Research Error: {e}"
                    )


# =====================================================
# WEB RESEARCH
# =====================================================

elif selected == "🌐 Web Research":

    st.title(
        "🌐 Web Research"
    )

    st.write(
        "Search the web and discover useful "
        "research sources."
    )


    web_query = st.text_input(

        "Search the web for research sources",

        placeholder=(
            "Example: Artificial Intelligence "
            "in Education"
        ),

        value=st.session_state.web_query
    )


    if st.button(
        "🔎 Search Web"
    ):

        if not web_query:

            st.warning(
                "Please enter a search topic."
            )

        else:

            with st.spinner(
                "🌐 Searching the web..."
            ):

                try:

                    results = search_web(
                        web_query
                    )


                    st.session_state.web_results = (
                        results
                    )


                    st.session_state.web_query = (
                        web_query
                    )


                    st.session_state.ai_summary = (
                        ""
                    )


                except Exception as e:

                    st.error(
                        f"Web Search Error: {e}"
                    )


    # -------------------------------------------------
    # DISPLAY WEB RESULTS
    # -------------------------------------------------

    if st.session_state.web_results:

        web_results = (
            st.session_state.web_results
        )


        st.success(
            f"Found {len(web_results)} web sources."
        )


        for i, result in enumerate(

            web_results,

            start=1

        ):

            title = result.get(
                "title",
                "Untitled Source"
            )


            url = result.get(
                "url",
                ""
            )


            snippet = result.get(
                "snippet",
                "No description available."
            )


            st.markdown(
                f"### {i}. {title}"
            )


            st.write(
                snippet
            )


            if url:

                st.markdown(
                    f"🔗 **[Open Source]({url})**"
                )


                st.caption(
                    f"Source URL: {url}"
                )


            st.divider()


        # -------------------------------------------------
        # AI SUMMARY
        # -------------------------------------------------

        st.subheader(
            "🤖 AI Research Summary"
        )


        st.write(
            "Generate an AI-powered research "
            "summary from the web sources above."
        )


        if st.button(
            "🤖 Generate AI Summary"
        ):

            with st.spinner(
                "🤖 Gemini is analyzing the web sources..."
            ):

                try:

                    sources_text = ""


                    for i, result in enumerate(

                        web_results,

                        start=1

                    ):

                        title = result.get(
                            "title",
                            ""
                        )


                        url = result.get(
                            "url",
                            ""
                        )


                        snippet = result.get(
                            "snippet",
                            ""
                        )


                        sources_text += f"""

SOURCE {i}

Title:
{title}

URL:
{url}

Content:
{snippet}

--------------------------------
"""


                    prompt = f"""
You are an AI Research Assistant.

Research Topic:

{st.session_state.web_query}

Analyze the web sources provided below.

{sources_text}

Create a professional research summary.

Use these sections:

# Research Overview

# Key Findings

# Major Concepts

# Applications

# Challenges

# Research Gaps

# Future Scope

# Conclusion

# References

For References:

- Include the source title.
- Include the original source URL.
- Do not invent sources.
- Use only the information provided.

Important:

- Do not invent facts.
- Do not create fake references.
- Do not add sources that were not provided.
- Use professional academic language.
- Make the report useful for students and researchers.
"""


                    response = client.models.generate_content(

                        model="gemini-2.5-flash",

                        contents=prompt
                    )


                    ai_summary = response.text


                    st.session_state.ai_summary = (
                        ai_summary
                    )


                    st.success(
                        "AI Research Summary Generated!"
                    )


                except Exception as e:

                    st.error(
                        f"AI Summary Error: {e}"
                    )


        # -------------------------------------------------
        # DISPLAY AI SUMMARY
        # -------------------------------------------------

        if st.session_state.ai_summary:

            st.divider()


            st.markdown(
                st.session_state.ai_summary
            )


            # ---------------------------------------------
            # TXT DOWNLOAD
            # ---------------------------------------------

            st.download_button(

                "📥 Download AI Research Summary",

                st.session_state.ai_summary,

                file_name=(
                    "ai_research_summary.txt"
                ),

                mime="text/plain"
            )


            # ---------------------------------------------
            # PDF GENERATION
            # ---------------------------------------------

            try:

                pdf_file = create_research_pdf(

                    title=(
                        "AI Research Report"
                    ),

                    topic=(
                        st.session_state.web_query
                    ),

                    content=(
                        st.session_state.ai_summary
                    ),

                    sources=web_results
                )


                st.download_button(

                    "📄 Download Professional Research PDF",

                    data=pdf_file,

                    file_name=(
                        "AI_Research_Report.pdf"
                    ),

                    mime="application/pdf"
                )


            except Exception as e:

                st.error(
                    f"PDF Generation Error: {e}"
                )


    else:

        st.info(
            "Enter a research topic and click "
            "'Search Web' to discover sources."
        )


# =====================================================
# PDF ANALYZER
# =====================================================

elif selected == "📄 PDF Analyzer":

    st.title(
        "📄 Research Paper Analyzer"
    )

    st.write(
        "Upload a research paper PDF and analyze "
        "it using Gemini AI."
    )


    uploaded_file = st.file_uploader(

        "Upload Research Paper",

        type=["pdf"]
    )


    if uploaded_file:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )


        if st.button(
            "📖 Extract & Analyze PDF"
        ):

            with st.spinner(
                "📄 Reading PDF..."
            ):

                try:

                    reader = PdfReader(
                        uploaded_file
                    )


                    extracted_text = ""


                    for page in reader.pages:

                        text = page.extract_text()


                        if text:

                            extracted_text += (
                                text + "\n"
                            )


                    st.session_state.pdf_text = (
                        extracted_text
                    )


                    st.success(

                        f"Extracted "
                        f"{len(extracted_text)} characters."

                    )


                except Exception as e:

                    st.error(
                        f"PDF Extraction Error: {e}"
                    )


            if st.session_state.pdf_text:

                with st.spinner(
                    "🤖 Gemini is analyzing the paper..."
                ):

                    try:

                        prompt = f"""
Analyze this research paper.

Provide:

1. Paper Summary
2. Research Objective
3. Methodology
4. Key Findings
5. Important Contributions
6. Limitations
7. Research Gaps
8. Future Scope
9. Possible Research Questions

Research Paper:

{st.session_state.pdf_text[:50000]}
"""


                        response = client.models.generate_content(

                            model="gemini-2.5-flash",

                            contents=prompt
                        )


                        analysis = response.text


                        st.session_state.pdf_analysis = (
                            analysis
                        )


                    except Exception as e:

                        st.error(
                            f"PDF Analysis Error: {e}"
                        )


    if st.session_state.pdf_analysis:

        st.divider()


        st.subheader(
            "🤖 AI Paper Analysis"
        )


        st.markdown(
            st.session_state.pdf_analysis
        )


        st.download_button(

            "📥 Download Analysis",

            st.session_state.pdf_analysis,

            file_name=(
                "research_paper_analysis.txt"
            ),

            mime="text/plain"
        )


# =====================================================
# ASK AI
# =====================================================

elif selected == "💬 Ask AI":

    st.title(
        "💬 Ask AI About Research Paper"
    )

    st.write(
        "Upload a PDF and ask questions about it."
    )


    uploaded_file = st.file_uploader(

        "Upload PDF",

        type=["pdf"],

        key="ask_ai_pdf"
    )


    if uploaded_file:

        if st.button(

            "📖 Read PDF",

            key="read_ask_pdf"

        ):

            with st.spinner(
                "Reading PDF..."
            ):

                try:

                    reader = PdfReader(
                        uploaded_file
                    )


                    text = ""


                    for page in reader.pages:

                        page_text = (
                            page.extract_text()
                        )


                        if page_text:

                            text += (
                                page_text + "\n"
                            )


                    st.session_state.pdf_text = (
                        text
                    )


                    st.success(
                        "PDF loaded successfully!"
                    )


                except Exception as e:

                    st.error(
                        f"PDF Error: {e}"
                    )


    if st.session_state.pdf_text:

        question = st.text_input(

            "Ask a question about the PDF",

            placeholder=(
                "Example: What is the main "
                "research objective?"
            )
        )


        if st.button(
            "🤖 Ask AI"
        ):

            if not question:

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "🤖 AI is thinking..."
                ):

                    try:

                        prompt = f"""
You are an AI research assistant.

Answer the user's question using
only the provided research paper.

Research Paper:

{st.session_state.pdf_text[:50000]}

Question:

{question}

Instructions:

- Give a clear answer.
- Do not invent information.
- If the answer is not available
  in the paper, say so.
"""


                        response = client.models.generate_content(

                            model="gemini-2.5-flash",

                            contents=prompt
                        )


                        st.markdown(
                            "### 🤖 AI Answer"
                        )


                        st.write(
                            response.text
                        )


                    except Exception as e:

                        st.error(
                            f"AI Error: {e}"
                        )
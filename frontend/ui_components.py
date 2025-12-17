"""
UI helper components
"""
import streamlit as st
from typing import Dict, List, Tuple


def display_chat_message(role: str, content: str, confidence: float = None):
    """Display a chat message"""
    if role == "user":
        st.write(f"👤 **You:** {content}")
    else:
        st.write(f"🤖 **Chatbot:** {content}")
        if confidence:
            confidence_level = get_confidence_badge(confidence)
            st.caption(f"Confidence: {confidence:.2%} {confidence_level}")


def get_confidence_badge(confidence: float) -> str:
    """Get emoji badge for confidence level"""
    if confidence >= 0.9:
        return "🟢 Very High"
    elif confidence >= 0.7:
        return "🟢 High"
    elif confidence >= 0.5:
        return "🟡 Medium"
    elif confidence >= 0.3:
        return "🟠 Low"
    else:
        return "🔴 Very Low"


def display_intent_card(intent: str, confidence: float):
    """Display intent detection card"""
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Intent", intent.upper())
        with col2:
            st.metric("Confidence", f"{confidence:.2%}")
        with col3:
            st.metric("Status", "✅ Confident" if confidence >= 0.5 else "⚠️ Low")


def display_chat_history(messages: List[Dict]):
    """Display chat history"""
    st.subheader("Chat History")
    if messages:
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            confidence = msg.get("confidence", None)
            display_chat_message(role, content, confidence)
    else:
        st.info("No messages yet. Start a conversation!")


def display_stats_dashboard(stats: Dict):
    """Display statistics dashboard"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Chats",
            stats.get("total_chats", 0),
            delta=None
        )

    with col2:
        st.metric(
            "Low Confidence Queries",
            stats.get("low_confidence_queries", 0),
            delta=None
        )

    with col3:
        avg_conf = stats.get("average_confidence", 0.0)
        st.metric(
            "Avg Confidence",
            f"{avg_conf:.2%}",
            delta=None
        )


def display_intent_options():
    """Display available intent options"""
    intents = {
        "📚 Courses": "Tell me about the courses offered",
        "🎓 Admissions": "How do I apply for admission?",
        "👨‍🏫 Faculty": "Tell me about the faculty",
        "📞 Contact": "How can I contact the college?",
        "ℹ️ About": "Tell me about the college",
        "🏫 Academics": "What about academics?",
    }

    st.subheader("Quick Questions")
    cols = st.columns(2)
    for idx, (emoji_label, question) in enumerate(intents.items()):
        with cols[idx % 2]:
            if st.button(emoji_label, key=f"intent_{idx}", use_container_width=True):
                return question

    return None


def display_error_message(error: str):
    """Display error message"""
    st.error(f"❌ Error: {error}")


def display_success_message(message: str):
    """Display success message"""
    st.success(f"✅ {message}")


def display_info_message(message: str):
    """Display info message"""
    st.info(f"ℹ️ {message}")

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="TechFlow AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .stChatMessage {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
    }
    
    .stChatMessage[data-testid="chat-message-assistant"] {
        background-color: #e3f2fd;
        border-left: 4px solid #667eea;
    }
    
    .chat-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea, #764ba2);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .status-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        background-color: #4CAF50;
        border-radius: 50%;
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Gemini AI
@st.cache_resource
def initialize_gemini():
    """Initialize Gemini AI model"""
    try:
        # Get API key from Streamlit secrets or environment variable
        api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            st.error("⚠️ Gemini API key not found! Please add it to your secrets or environment variables.")
            st.info("Add your API key to `.streamlit/secrets.toml` as: `GEMINI_API_KEY = 'your-api-key'`")
            return None
            
        genai.configure(api_key=api_key)
        
        # Configure the model with system instructions
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            generation_config=generation_config,
            system_instruction="""You are a helpful AI assistant for TechFlow Solutions, 
            an IT company specializing in web development, cloud solutions, AI integration, 
            mobile apps, cybersecurity, and data analytics. Be professional, friendly, and 
            knowledgeable about technology. Help users with their questions about our services, 
            provide technical guidance, and assist with general IT inquiries."""
        )
        
        return model
        
    except Exception as e:
        st.error(f"Error initializing Gemini: {str(e)}")
        return None

# Initialize session state
def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I'm your AI assistant powered by Gemini 2.0 Flash. I'm here to help you with questions about TechFlow Solutions' services, technical guidance, or any IT-related inquiries. How can I assist you today?"
            }
        ]
    
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = datetime.now()

def display_chat_header():
    """Display chat header with status"""
    st.markdown("""
    <div class="chat-header">
        <h2>🤖 TechFlow AI Assistant</h2>
        <p><span class="status-indicator"></span>Powered by Gemini 2.0 Flash - Online & Ready</p>
    </div>
    """, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar with information and controls"""
    with st.sidebar:
        st.markdown("### 🏢 TechFlow Solutions")
        st.markdown("**AI-Powered Customer Support**")
        
        st.markdown("---")
        st.markdown("### 📋 Quick Actions")
        
        if st.button("🔄 Clear Chat History"):
            st.session_state.messages = [
                {
                    "role": "assistant", 
                    "content": "Chat history cleared! How can I help you today?"
                }
            ]
            st.rerun()
        
        if st.button("🏠 Back to Main Website"):
            st.markdown("""
            <script>
                window.parent.location.href = 'index.html';
            </script>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💡 I can help with:")
        st.markdown("""
        - Web Development questions
        - Cloud Solutions guidance  
        - AI Integration advice
        - Mobile App development
        - Cybersecurity concerns
        - Data Analytics insights
        - General IT support
        """)
        
        st.markdown("---")
        st.markdown("### 📊 Session Info")
        if "conversation_started" in st.session_state:
            duration = datetime.now() - st.session_state.conversation_started
            st.write(f"**Duration:** {duration.seconds//60}m {duration.seconds%60}s")
        
        st.write(f"**Messages:** {len(st.session_state.messages)}")

def generate_response(model, prompt):
    """Generate response from Gemini model with error handling"""
    try:
        with st.spinner("🤔 Thinking..."):
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        error_msg = f"Sorry, I encountered an error: {str(e)}"
        st.error(error_msg)
        return "I apologize, but I'm having trouble processing your request right now. Please try again or contact our support team directly."

def main():
    """Main application function"""
    # Initialize
    initialize_session_state()
    model = initialize_gemini()
    
    # Display UI
    display_chat_header()
    display_sidebar()
    
    # Check if model is initialized
    if not model:
        st.stop()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about TechFlow's services or IT in general..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            response = generate_response(model, prompt)
            st.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer
    st.markdown("""
    <div class="footer">
        Powered by Gemini 2.0 Flash | TechFlow Solutions © 2024 | 
        <a href="mailto:support@techflow.com">Contact Support</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

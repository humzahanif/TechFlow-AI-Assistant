# import streamlit as st
# import google.generativeai as genai
# import os
# from datetime import datetime
# import time

# # Page configuration
# st.set_page_config(
#     page_title="TechFlow AI Assistant",
#     page_icon="🤖",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main > div {
#         padding-top: 2rem;
#     }
    
#     .stChatMessage {
#         background-color: #f8f9fa;
#         border-radius: 10px;
#         padding: 1rem;
#         margin: 0.5rem 0;
#     }
    
#     .stChatMessage[data-testid="chat-message-user"] {
#         background: linear-gradient(45deg, #667eea, #764ba2);
#         color: white;
#     }
    
#     .stChatMessage[data-testid="chat-message-assistant"] {
#         background-color: #e3f2fd;
#         border-left: 4px solid #667eea;
#     }
    
#     .chat-header {
#         text-align: center;
#         padding: 1rem;
#         background: linear-gradient(45deg, #667eea, #764ba2);
#         color: white;
#         border-radius: 10px;
#         margin-bottom: 2rem;
#     }
    
#     .sidebar .sidebar-content {
#         background: linear-gradient(180deg, #667eea, #764ba2);
#     }
    
#     .stButton > button {
#         background: linear-gradient(45deg, #667eea, #764ba2);
#         color: white;
#         border: none;
#         border-radius: 20px;
#         padding: 0.5rem 1rem;
#         transition: all 0.3s ease;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
#     }
    
#     .status-indicator {
#         display: inline-block;
#         width: 8px;
#         height: 8px;
#         background-color: #4CAF50;
#         border-radius: 50%;
#         margin-right: 8px;
#         animation: pulse 2s infinite;
#     }
    
#     @keyframes pulse {
#         0% { opacity: 1; }
#         50% { opacity: 0.5; }
#         100% { opacity: 1; }
#     }
    
#     .footer {
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         right: 0;
#         background: rgba(255, 255, 255, 0.9);
#         backdrop-filter: blur(10px);
#         text-align: center;
#         padding: 10px;
#         font-size: 12px;
#         color: #666;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Initialize Gemini AI
# @st.cache_resource
# def initialize_gemini():
#     """Initialize Gemini AI model"""
#     try:
#         # Get API key from Streamlit secrets or environment variable
#         # api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
#         api_key = ""
        
#         # if not api_key:
#         #     st.error("⚠️ Gemini API key not found! Please add it to your secrets or environment variables.")
#         #     st.info("Add your API key to `.streamlit/secrets.toml` as: `GEMINI_API_KEY = 'your-api-key'`")
#         #     return None
            
#         genai.configure(api_key=api_key)
        
#         # Configure the model with system instructions
#         generation_config = {
#             "temperature": 0.7,
#             "top_p": 0.8,
#             "top_k": 40,
#             "max_output_tokens": 2048,
#         }
        
#         model = genai.GenerativeModel(
#             model_name='gemini-2.0-flash-exp',
#             generation_config=generation_config,
#             system_instruction="""You are a helpful AI assistant for TechFlow Solutions, 
#             an IT company specializing in web development, cloud solutions, AI integration, 
#             mobile apps, cybersecurity, and data analytics. Be professional, friendly, and 
#             knowledgeable about technology. Help users with their questions about our services, 
#             provide technical guidance, and assist with general IT inquiries."""
#         )
        
#         return model
        
#     except Exception as e:
#         st.error(f"Error initializing Gemini: {str(e)}")
#         return None

# # Initialize session state
# def initialize_session_state():
#     """Initialize session state variables"""
#     if "messages" not in st.session_state:
#         st.session_state.messages = [
#             {
#                 "role": "assistant",
#                 "content": "Hello! I'm your AI assistant powered by Gemini 2.0 Flash. I'm here to help you with questions about TechFlow Solutions' services, technical guidance, or any IT-related inquiries. How can I assist you today?"
#             }
#         ]
    
#     if "conversation_started" not in st.session_state:
#         st.session_state.conversation_started = datetime.now()

# def display_chat_header():
#     """Display chat header with status"""
#     st.markdown("""
#     <div class="chat-header">
#         <h2>🤖 TechFlow AI Assistant</h2>
#         <p><span class="status-indicator"></span>Powered by Gemini 2.0 Flash - Online & Ready</p>
#     </div>
#     """, unsafe_allow_html=True)

# def display_sidebar():
#     """Display sidebar with information and controls"""
#     with st.sidebar:
#         st.markdown("### 🏢 TechFlow Solutions")
#         st.markdown("**AI-Powered Customer Support**")
        
#         st.markdown("---")
#         st.markdown("### 📋 Quick Actions")
        
#         if st.button("🔄 Clear Chat History"):
#             st.session_state.messages = [
#                 {
#                     "role": "assistant", 
#                     "content": "Chat history cleared! How can I help you today?"
#                 }
#             ]
#             st.rerun()
        
#         if st.button("🏠 Back to Main Website"):
#             st.markdown("""
#             <script>
#                 window.parent.location.href = 'index.html';
#             </script>
#             """, unsafe_allow_html=True)
        
#         st.markdown("---")
#         st.markdown("### 💡 I can help with:")
#         st.markdown("""
#         - Web Development questions
#         - Cloud Solutions guidance  
#         - AI Integration advice
#         - Mobile App development
#         - Cybersecurity concerns
#         - Data Analytics insights
#         - General IT support
#         """)
        
#         st.markdown("---")
#         st.markdown("### 📊 Session Info")
#         if "conversation_started" in st.session_state:
#             duration = datetime.now() - st.session_state.conversation_started
#             st.write(f"**Duration:** {duration.seconds//60}m {duration.seconds%60}s")
        
#         st.write(f"**Messages:** {len(st.session_state.messages)}")

# def generate_response(model, prompt):
#     """Generate response from Gemini model with error handling"""
#     try:
#         with st.spinner("🤔 Thinking..."):
#             response = model.generate_content(prompt)
#             return response.text
#     except Exception as e:
#         error_msg = f"Sorry, I encountered an error: {str(e)}"
#         st.error(error_msg)
#         return "I apologize, but I'm having trouble processing your request right now. Please try again or contact our support team directly."

# def main():
#     """Main application function"""
#     # Initialize
#     initialize_session_state()
#     model = initialize_gemini()
    
#     # Display UI
#     display_chat_header()
#     display_sidebar()
    
#     # Check if model is initialized
#     if not model:
#         st.stop()
    
#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
    
#     # Chat input
#     if prompt := st.chat_input("Ask me anything about TechFlow's services or IT in general..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         # Display user message
#         with st.chat_message("user"):
#             st.markdown(prompt)
        
#         # Generate and display assistant response
#         with st.chat_message("assistant"):
#             response = generate_response(model, prompt)
#             st.markdown(response)
            
#             # Add assistant response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": response})
    
#     # Footer
#     st.markdown("""
#     <div class="footer">
#         Powered by Gemini 2.0 Flash | TechFlow Solutions © 2024 | 
#         <a href="mailto:support@techflow.com">Contact Support</a>
#     </div>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="TechFlow AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS for both light and dark mode compatibility
st.markdown("""
<style>
    /* CSS Variables for theme-aware colors */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --gradient: linear-gradient(45deg, #667eea, #764ba2);
        --text-primary: #1f2937;
        --text-secondary: #6b7280;
        --bg-primary: #ffffff;
        --bg-secondary: #f8f9fa;
        --bg-card: #ffffff;
        --border-color: #e5e7eb;
        --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Dark mode variables */
    [data-theme="dark"], .dark {
        --text-primary: #f9fafb;
        --text-secondary: #d1d5db;
        --bg-primary: #111827;
        --bg-secondary: #1f2937;
        --bg-card: #374151;
        --border-color: #4b5563;
        --shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }
    
    /* Auto-detect dark mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --text-primary: #f9fafb;
            --text-secondary: #d1d5db;
            --bg-primary: #111827;
            --bg-secondary: #1f2937;
            --bg-card: #374151;
            --border-color: #4b5563;
            --shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
    }
    
    /* Main container adjustments */
    .main > div {
        padding-top: 2rem;
        color: var(--text-primary);
    }
    
    /* Chat message styling with theme awareness */
    .stChatMessage {
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color);
        border-radius: 12px !important;
        padding: 1rem !important;
        margin: 0.75rem 0 !important;
        box-shadow: var(--shadow);
        transition: all 0.2s ease;
    }
    
    .stChatMessage:hover {
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
        transform: translateY(-1px);
    }
    
    /* User message styling */
    .stChatMessage[data-testid="chat-message-user"] {
        background: var(--gradient) !important;
        color: white !important;
        border: none;
        position: relative;
        overflow: hidden;
    }
    
    .stChatMessage[data-testid="chat-message-user"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, 
            rgba(255,255,255,0.1), 
            transparent, 
            rgba(255,255,255,0.1));
        pointer-events: none;
    }
    
    /* Assistant message styling */
    .stChatMessage[data-testid="chat-message-assistant"] {
        background-color: var(--bg-card) !important;
        border-left: 4px solid var(--primary-color);
        color: var(--text-primary) !important;
    }
    
    /* Chat header with improved dark mode support */
    .chat-header {
        text-align: center;
        padding: 2rem 1rem;
        background: var(--gradient);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }
    
    .chat-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, 
            rgba(255,255,255,0.1), 
            transparent, 
            rgba(255,255,255,0.1));
        animation: shimmer 3s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { opacity: 0; }
        50% { opacity: 1; }
    }
    
    .chat-header h2 {
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .chat-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
    }
    
    /* Service highlight with theme support */
    .service-highlight {
        background: linear-gradient(135deg, 
            rgba(102, 126, 234, 0.1), 
            rgba(118, 75, 162, 0.05));
        border-left: 4px solid var(--primary-color);
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
        color: var(--text-primary);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .service-highlight:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
    }
    
    /* Package info with enhanced styling */
    .package-info {
        background: var(--bg-card);
        border: 2px solid var(--primary-color);
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        color: var(--text-primary);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .package-info::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--gradient);
    }
    
    .package-info:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }
    
    /* Contact info with dark mode support */
    .contact-info {
        background: var(--bg-card);
        color: var(--text-primary);
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow);
    }
    
    /* Team member tags */
    .team-member {
        display: inline-block;
        background: var(--bg-secondary);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        padding: 8px 16px;
        border-radius: 25px;
        margin: 5px;
        font-size: 0.9em;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    
    .team-member:hover {
        background: var(--gradient);
        color: white;
        transform: scale(1.05);
    }
    
    /* Sidebar styling improvements */
    .css-1d391kg {
        background-color: var(--bg-secondary);
    }
    
    /* Button styling for dark mode */
    .stButton > button {
        background: var(--gradient) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Input styling for dark mode */
    .stTextInput > div > div > input {
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
    }
    
    /* Chat input styling */
    .stChatInput > div {
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 25px !important;
    }
    
    /* Footer styling */
    .footer-info {
        text-align: center;
        padding: 25px;
        background: var(--bg-card);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: var(--shadow);
    }
    
    /* Responsive design improvements */
    @media (max-width: 768px) {
        .chat-header h2 {
            font-size: 1.5rem;
        }
        
        .chat-header p {
            font-size: 1rem;
        }
        
        .service-highlight,
        .package-info,
        .contact-info {
            margin: 10px 0;
            padding: 12px;
        }
    }
    
    /* Scrollbar styling for dark mode */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary-color);
    }
    
    /* Loading spinner styling */
    .stSpinner > div {
        border-color: var(--primary-color) !important;
    }
    
    /* Success/Error message styling */
    .stAlert {
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
    }
</style>
""", unsafe_allow_html=True)

# TechFlow Solutions Knowledge Base (unchanged)
TECHFLOW_KNOWLEDGE = {
    "company_info": {
        "name": "TechFlow Solutions",
        "tagline": "Innovative IT Solutions - Transforming businesses through cutting-edge technology and exceptional service",
        "description": "Leading IT company specializing in digital transformation and innovative technology solutions with over a decade of experience",
        "stats": {
            "projects_completed": "500+",
            "happy_clients": "200+",
            "team_members": "50+",
            "years_experience": "10+"
        }
    },
    
    "services": {
        "web_development": {
            "name": "Web Development",
            "description": "Custom web applications built with modern technologies and responsive design for optimal user experience",
            "icon": "💻"
        },
        "cloud_solutions": {
            "name": "Cloud Solutions", 
            "description": "Scalable cloud infrastructure and migration services to improve efficiency and reduce operational costs",
            "icon": "☁️"
        },
        "ai_integration": {
            "name": "AI Integration",
            "description": "Intelligent automation and AI-powered solutions to streamline business processes and enhance productivity", 
            "icon": "🤖"
        },
        "mobile_apps": {
            "name": "Mobile Apps",
            "description": "Native and cross-platform mobile applications for iOS and Android with seamless user experiences",
            "icon": "📱"
        },
        "cybersecurity": {
            "name": "Cybersecurity",
            "description": "Comprehensive security solutions to protect your business from digital threats and data breaches",
            "icon": "🔒"
        },
        "data_analytics": {
            "name": "Data Analytics", 
            "description": "Transform raw data into actionable insights with advanced analytics and business intelligence tools",
            "icon": "📊"
        }
    },
    
    "packages": {
        "starter": {
            "name": "Starter",
            "price": "$99/month",
            "features": [
                "Basic website (up to 5 pages)",
                "Mobile responsive design", 
                "SEO optimization",
                "Contact form integration",
                "1 month free support",
                "SSL certificate"
            ]
        },
        "professional": {
            "name": "Professional", 
            "price": "$299/month",
            "popular": True,
            "features": [
                "Custom web application",
                "Database integration",
                "Admin dashboard", 
                "API development",
                "Cloud deployment",
                "3 months free support",
                "Performance monitoring",
                "Security hardening"
            ]
        },
        "enterprise": {
            "name": "Enterprise",
            "price": "$799/month", 
            "features": [
                "Full-scale application",
                "Microservices architecture",
                "AI/ML integration",
                "DevOps pipeline",
                "24/7 monitoring",
                "6 months free support", 
                "Custom integrations",
                "Dedicated account manager"
            ]
        }
    },
    
    "team": {
        "alex_rodriguez": "Alex Rodriguez - Chief Technology Officer (15+ years in software architecture and AI development)",
        "sarah_chen": "Sarah Chen - Lead Full Stack Developer (Expert in React, Node.js, and cloud technologies)",
        "michael_thompson": "Michael Thompson - UI/UX Design Lead (10+ years creating intuitive interfaces)",
        "emily_watson": "Dr. Emily Watson - AI/ML Specialist (PhD in Machine Learning, develops intelligent systems)",
        "james_wilson": "James Wilson - Cybersecurity Expert (Certified security professional)",
        "lisa_park": "Lisa Park - Project Manager (Agile certified project manager)"
    },
    
    "contact": {
        "address": "123 Tech Boulevard, Innovation District, Karachi, Sindh 75500, Pakistan",
        "phone": "+92 21 1234-5678",
        "mobile": "+92 300 1234567",
        "email": "info@techflowsolutions.com",
        "support_email": "support@techflowsolutions.com", 
        "hours": "Mon-Fri: 9:00 AM - 6:00 PM, Sat: 10:00 AM - 2:00 PM"
    }
}

# Initialize Gemini AI with enhanced system prompt
@st.cache_resource
def initialize_gemini():
    """Initialize Gemini AI model with TechFlow-specific knowledge"""
    try:
        api_key = "AIzaSyBJOTWqYl-TGl8sFSPUPLCOENsrqaTd1Ng"
        genai.configure(api_key=api_key)
        
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        # Enhanced system instruction with company knowledge
        system_instruction = f"""You are the official AI assistant for TechFlow Solutions. You have comprehensive knowledge about the company and should provide accurate, helpful responses based on the following information:

COMPANY OVERVIEW:
{json.dumps(TECHFLOW_KNOWLEDGE, indent=2)}

GUIDELINES:
1. Always respond as TechFlow Solutions' representative
2. Use the exact company information provided above
3. When discussing services, mention specific features and benefits
4. For pricing questions, refer to our three packages: Starter ($99/month), Professional ($299/month - Most Popular), and Enterprise ($799/month)
5. For team questions, mention our expert team members by name and expertise
6. Provide contact information when requested
7. Be professional but friendly, and always try to guide users toward our services
8. If asked about competitors, focus on TechFlow's strengths instead
9. For technical questions outside our services, provide helpful general guidance
10. Always encourage users to contact us for detailed consultations

Remember: You represent TechFlow Solutions - be knowledgeable, professional, and helpful while promoting our services appropriately."""

        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            generation_config=generation_config,
            system_instruction=system_instruction
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
                "content": """Hello! I'm your TechFlow Solutions AI assistant. I'm here to help you with:

🔷 **Our Services**: Web Development, Cloud Solutions, AI Integration, Mobile Apps, Cybersecurity, and Data Analytics

🔷 **Pricing & Packages**: From our Starter package ($99/month) to Enterprise solutions ($799/month)

🔷 **Our Expert Team**: Get to know our specialists and their expertise

🔷 **Technical Guidance**: General IT advice and best practices

🔷 **Contact & Support**: Connect with our team for personalized assistance

What would you like to know about TechFlow Solutions today?"""
            }
        ]
    
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = datetime.now()

def display_chat_header():
    """Display chat header with TechFlow branding"""
    st.markdown("""
    <div class="chat-header">
        <h2>🤖 TechFlow Solutions AI Assistant</h2>
        <p>Powered by Gemini 2.0 Flash | Your Technology Partner Since 2014</p>
    </div>
    """, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar with TechFlow information"""
    with st.sidebar:
        st.markdown("### 🏢 TechFlow Solutions")
        st.markdown("**Innovative IT Services**")
        st.markdown("*Transforming businesses through technology*")
        
        st.markdown("---")
        st.markdown("### 🚀 Our Services")
        services = [
            "💻 Web Development",
            "☁️ Cloud Solutions", 
            "🤖 AI Integration",
            "📱 Mobile Apps",
            "🔒 Cybersecurity",
            "📊 Data Analytics"
        ]
        for service in services:
            st.markdown(f"- {service}")
        
        st.markdown("---")
        st.markdown("### 📦 Packages")
        st.markdown("- **Starter**: $99/month")
        st.markdown("- **Professional**: $299/month ⭐") 
        st.markdown("- **Enterprise**: $799/month")
        
        st.markdown("---")
        st.markdown("### 📞 Contact Us")
        st.markdown("📧 info@techflowsolutions.com")
        st.markdown("📱 +92 300 1234567")
        st.markdown("🕒 Mon-Fri: 9AM-6PM")
        
        st.markdown("---")
        if st.button("🔄 Clear Chat"):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "Chat cleared! How can TechFlow Solutions help you today?"
                }
            ]
            st.rerun()
        
        if st.button("🏠 Visit Main Website"):
            st.markdown("""
            <script>
                if (window.parent !== window) {
                    window.parent.postMessage('close_chat', '*');
                } else {
                    window.open('/', '_blank');
                }
            </script>
            """, unsafe_allow_html=True)

def enhance_response_with_formatting(response_text):
    """Add visual formatting to responses based on content"""
    
    # Check if response mentions services and format them
    for service_key, service_info in TECHFLOW_KNOWLEDGE["services"].items():
        if service_info["name"].lower() in response_text.lower():
            service_highlight = f"""
            <div class="service-highlight">
                <strong>{service_info["icon"]} {service_info["name"]}</strong><br>
                {service_info["description"]}
            </div>
            """
            response_text = response_text.replace(
                service_info["name"], 
                f"{service_info['name']}"
            )
    
    # Check if response mentions packages
    for package_key, package_info in TECHFLOW_KNOWLEDGE["packages"].items():
        if package_info["name"].lower() in response_text.lower():
            popular_badge = " ⭐ POPULAR" if package_info.get("popular", False) else ""
            package_highlight = f"""
            <div class="package-info">
                <strong>{package_info["name"]}{popular_badge}</strong> - {package_info["price"]}<br>
                Key features: {", ".join(package_info["features"][:3])}...
            </div>
            """
    
    return response_text

def generate_response(model, prompt):
    """Generate response from Gemini model with TechFlow context"""
    try:
        with st.spinner("Analyzing your request..."):
            # Add context about what type of information the user might be seeking
            enhanced_prompt = f"""
            User Query: {prompt}
            
            Context: This is a query to TechFlow Solutions. Please provide a comprehensive response using the company knowledge provided in your system instructions. If the query is about:
            - Services: Provide detailed information about relevant services
            - Pricing: Mention our packages with specific pricing
            - Team: Reference specific team members and their expertise  
            - Contact: Provide complete contact information
            - Technical advice: Give helpful guidance while relating it back to our services when relevant
            """
            
            response = model.generate_content(enhanced_prompt)
            return response.text
            
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return """I apologize for the technical difficulty. Please feel free to contact TechFlow Solutions directly:

📧 **Email**: info@techflowsolutions.com
📞 **Phone**: +92 21 1234-5678  
📱 **Mobile**: +92 300 1234567

Our team is available Mon-Fri: 9:00 AM - 6:00 PM to assist you personally."""

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
        st.error("Unable to initialize AI assistant. Please contact support.")
        st.stop()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                # Apply formatting to assistant messages
                formatted_content = enhance_response_with_formatting(message["content"])
                st.markdown(formatted_content, unsafe_allow_html=True)
            else:
                st.markdown(message["content"])
    
    # Chat input with placeholder
    if prompt := st.chat_input("Ask about our services, pricing, team, or any IT questions..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            response = generate_response(model, prompt)
            formatted_response = enhance_response_with_formatting(response)
            st.markdown(formatted_response, unsafe_allow_html=True)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer with company info
    st.markdown("---")
    st.markdown("""
    <div class="footer-info">
        <strong>🏢 TechFlow Solutions</strong> - Your Technology Partner<br>
        📧 info@techflowsolutions.com | 📞 +92 21 1234-5678<br>
        <small>Available Mon-Fri: 9AM-6PM | Karachi, Pakistan</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

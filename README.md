# ReHearten - AI-Powered Emotional Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://djangoproject.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-blue.svg)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Overview

**ReHearten** is a cutting-edge AI-powered emotional intelligence platform designed to help users understand, manage, and enhance their emotional well-being. Built with modern web technologies and powered by advanced AI models, ReHearten provides a comprehensive solution for emotional intelligence development.

### 🎯 Mission
To empower individuals with AI-driven tools for emotional intelligence, fostering better mental health and interpersonal relationships through technology.

## ✨ Features

### 🔐 Authentication & User Management
- **Multi-role User System**: Admin and regular user roles with different permissions
- **Google OAuth2 Integration**: Seamless login with Google accounts
- **Secure Session Management**: Custom session handling with MongoDB
- **User Profile Management**: Complete user profile editing and management
- **Password Security**: Secure password hashing and change functionality

### 🤖 AI-Powered Features
- **Emotional Intelligence Analysis**: AI-driven emotional assessment and insights
- **Personalized Recommendations**: Tailored suggestions based on user emotional patterns
- **Interactive AI Conversations**: Natural language processing for emotional support
- **Progress Tracking**: Monitor emotional intelligence development over time

### 🎨 Modern User Interface
- **Responsive Design**: Beautiful, modern UI that works on all devices
- **Animated Backgrounds**: Engaging video and gradient backgrounds
- **ChatGPT-style Interface**: Clean, intuitive user experience
- **Real-time Updates**: Dynamic content updates without page refresh
- **Accessibility**: Designed with accessibility best practices

### 🔧 Technical Features
- **MongoDB Integration**: NoSQL database for flexible data storage
- **RESTful API**: Comprehensive API endpoints for frontend-backend communication
- **Social Authentication**: Google OAuth2 integration
- **Session Management**: Custom session handling with security features
- **Admin Dashboard**: Comprehensive admin panel for user management

## 🛠️ Technology Stack

### Backend
- **Python 3.12+**: Core programming language
- **Django 4.2+**: Web framework for rapid development
- **Django REST Framework**: API development
- **MongoDB + MongoEngine**: NoSQL database with ODM
- **Social Auth**: OAuth2 authentication

### Frontend
- **Bootstrap 5.3**: Responsive CSS framework
- **Font Awesome 6**: Icon library
- **Inter Font**: Modern typography
- **Marked.js**: Markdown parsing
- **Custom CSS/JS**: Tailored styling and interactions

### AI & External Services
- **OpenAI API**: Advanced AI capabilities
- **Anthropic Claude**: Alternative AI model integration
- **Google OAuth2**: Social authentication

### Development Tools
- **Python-dotenv**: Environment variable management
- **Django Debug Toolbar**: Development debugging
- **Pillow**: Image processing
- **Cryptography**: Security features

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- MongoDB Atlas account (or local MongoDB)
- Google OAuth2 credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nguyenhieu277/rehearten.git
   cd rehearten
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or using uv (recommended)
   uv sync
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Database Configuration**
   - Set up MongoDB Atlas cluster
   - Update MongoDB connection string in `.env`
   - Configure Google OAuth2 credentials

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open http://localhost:8000
   - Login with your admin credentials

## 📁 Project Structure

```
ReHearten/
├── accounts/                 # User authentication and management
│   ├── models.py            # MongoDB user models
│   ├── views.py             # Authentication views
│   ├── forms.py             # User forms
│   ├── backends.py          # Custom authentication backends
│   └── management/          # Django management commands
├── REHEARTEN/               # Django project settings
│   ├── settings.py          # Main configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── templates/               # HTML templates
│   └── accounts/            # User interface templates
├── static/                  # Static files
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   ├── images/              # Images and logos
│   └── videos/              # Video assets
├── logs/                    # Application logs
├── manage.py                # Django management script
└── pyproject.toml           # Project dependencies
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MongoDB Configuration
MONGODB_URI=your-mongodb-atlas-connection-string
MONGODB_NAME=rehearten

# Google OAuth2
GOOGLE_OAUTH2_CLIENT_ID=your-google-client-id
GOOGLE_OAUTH2_CLIENT_SECRET=your-google-client-secret
``` 

### Google OAuth2 Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth2 credentials
5. Add authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`

## 👥 User Roles

### Admin Users
- Full system access
- User management capabilities
- System statistics and monitoring
- Content management

### Regular Users
- Personal profile management
- AI-powered emotional intelligence features
- Progress tracking
- Community features

## 🔒 Security Features

- **Password Hashing**: Secure password storage using Django's built-in hashers
- **Session Security**: Custom session management with MongoDB
- **CSRF Protection**: Cross-site request forgery protection
- **OAuth2 Security**: Secure social authentication
- **Input Validation**: Comprehensive form validation
- **SQL Injection Protection**: MongoDB ODM prevents injection attacks

## 🎨 UI/UX Features

- **Responsive Design**: Mobile-first approach
- **Modern Animations**: Smooth transitions and effects
- **Accessibility**: WCAG compliant design
- **Dark/Light Mode**: Theme switching capability
- **Loading States**: User feedback during operations
- **Error Handling**: Graceful error messages

## 📊 API Endpoints

### Authentication
- `POST /accounts/register/` - User registration
- `POST /accounts/login/` - User login
- `POST /accounts/logout/` - User logout
- `GET /accounts/profile/` - User profile

### User Management
- `GET /accounts/users/` - List users (admin only)
- `PUT /accounts/users/<id>/` - Update user (admin only)
- `DELETE /accounts/users/<id>/` - Delete user (admin only)

### AI Features
- `POST /api/emotional-analysis/` - Emotional intelligence analysis
- `GET /api/user-progress/` - User progress tracking
- `POST /api/ai-conversation/` - AI conversation endpoint

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False` in settings
2. Configure production database
3. Set up static file serving
4. Configure HTTPS
5. Set up monitoring and logging

### Docker Deployment
```bash
# Build and run with Docker
docker build -t rehearten .
docker run -p 8000:8000 rehearten
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PTIT (Posts and Telecommunications Institute of Technology)** - Academic partnership
- **OpenAI** - AI capabilities
- **Anthropic** - Alternative AI models
- **Django Community** - Web framework
- **MongoDB** - Database solution

## 📞 Support

- **Email**: support@rehearten.com
- **Documentation**: [docs.rehearten.com](https://docs.rehearten.com)
- **Issues**: [GitHub Issues](https://github.com/nguyenhieu277/rehearten/issues)

## 🔮 Roadmap

- [ ] Mobile app development
- [ ] Advanced AI emotional analysis
- [ ] Community features
- [ ] Integration with wearable devices
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

---

**Made with ❤️ by the ReHearten Team**

*Empowering emotional intelligence through AI technology*

# Personal Blog

A simple personal blog application where you can write and publish articles. Built with Python Flask using server-side rendering and filesystem-based storage.

**Project URL:** https://roadmap.sh/projects/personal-blog/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Public article viewing with clean, minimal design
- ✅ Admin authentication with session management
- ✅ Create, edit, and delete articles
- ✅ Markdown file storage (one file per article)
- ✅ CSRF protection on all forms
- ✅ Form validation with WTForms
- ✅ Dark theme with modern, minimal aesthetics
- ✅ Responsive design for mobile and desktop
- ✅ No database required

## Requirements

- Python 3.6 or higher
- Flask 3.1.2 or higher
- Flask-WTF for forms and CSRF protection
- python-dotenv for environment variables
- python-frontmatter for markdown parsing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd personal-blog
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install Flask Flask-WTF python-dotenv python-frontmatter
```

4. Create a `.env` file in the project root:
```bash
SECRET_KEY=your-super-secret-random-key-here
PASSWORD=your-admin-password-here
```

**Generate a secure secret key:**
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

## Project Structure

```
personal-blog/
├── articles/                   # Markdown files for articles (auto-created)
├── static/
│   └── style.css              # Dark theme styling
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── home.html              # Public homepage (article list)
│   ├── article.html           # Individual article view
│   ├── login.html             # Admin login page
│   ├── dashboard.html         # Admin dashboard
│   ├── add_article.html       # Create new article
│   └── edit_article.html      # Edit existing article
├── utils/
│   ├── article_manager.py     # CRUD operations for articles
│   └── auth.py                # Authentication logic
├── app.py                     # Main application file
├── .env                       # Environment variables (create this)
├── .gitignore
└── README.md
```

## Usage

1. Start the Flask development server:
```bash
flask run
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. **As a visitor:**
   - Browse published articles on the homepage
   - Click any article to read the full content

4. **As an admin:**
   - Click "Admin Login" in the navigation
   - Login with credentials from your `.env` file
   - Access the dashboard to manage articles
   - Create, edit, or delete articles

## Article Storage

Articles are stored as individual Markdown files with frontmatter in the `articles/` directory:

```markdown
---
title: My First Blog Post
date: 2026-01-11
---

This is the content of my blog post.

I can write multiple paragraphs here.
```

**File naming convention:**
- Format: `{timestamp}_{uuid4}.md`
- Example: `1736612345_a1b2c3d4e5f6.md`
- Ensures unique filenames and chronological ordering

## Authentication

- **Username:** `admin` (hardcoded)
- **Password:** Set in `.env` file
- **Session-based:** Login persists across pages
- **Protected routes:** Dashboard, create, edit, and delete require authentication

## Form Validation

The application validates article submissions:

- **Title:** 4-200 characters, required
- **Date:** Valid date format, required
- **Content:** 30-50,000 characters, required
- **CSRF Protection:** All forms include CSRF tokens

## Example Workflow

### Creating an Article

1. Login to the admin dashboard
2. Click "New Article" button
3. Fill in the form:
   - Title: "Getting Started with Python"
   - Date: Select today's date
   - Content: Write your article
4. Click "Publish Article"
5. Redirected to dashboard with success message
6. Article appears on public homepage

### Editing an Article

1. From the dashboard, click "Edit" next to an article
2. Modify any fields (title, date, or content)
3. Click "Update Article"
4. Changes are saved to the same file
5. View updated article on homepage

### Deleting an Article

1. From the dashboard, click "Delete" next to an article
2. Confirm deletion in the browser dialog
3. Article file is permanently removed
4. Redirected to dashboard with confirmation

## Security Features

- **CSRF Protection:** Flask-WTF protects all POST requests
- **Session Management:** Secure session cookies with secret key
- **Input Validation:** WTForms validates all form inputs
- **Protected Routes:** Decorator ensures authentication
- **Environment Variables:** Sensitive data not in source code

## Development

### Code Organization

- **app.py**: Flask routes and application configuration
- **utils/article_manager.py**: Article CRUD operations and file handling
- **utils/auth.py**: Authentication decorator and credential validation
- **templates/**: Jinja2 templates for all pages
- **static/**: CSS with dark, minimal design theme

### Best Practices Implemented

- ✅ Separation of concerns (routes, business logic, auth)
- ✅ Environment variables for secrets
- ✅ Form validation with WTForms
- ✅ CSRF protection on all forms
- ✅ Session-based authentication
- ✅ Unique article IDs with timestamp + UUID
- ✅ Error handling for missing articles
- ✅ Flash messages for user feedback

### Running in Debug Mode

```bash
flask --app app --debug run
```

## Future Enhancements

Potential improvements for learning:
- Add markdown rendering for formatted content
- Implement article categories or tags
- Add search functionality
- Support draft vs published status
- Add comment system
- Pagination for article list
- RSS feed generation
- Image upload support

## Troubleshooting

**Login not working:**
- Check `.env` file exists and contains `PASSWORD`
- Verify password is correct
- Check Flask secret key is set

**Articles not showing:**
- Verify `articles/` directory exists
- Check markdown files have correct frontmatter format
- Ensure date format is valid (YYYY-MM-DD)

**CSRF errors:**
- Ensure Flask-WTF is installed
- Check `{{ form.csrf_token }}` is in all forms
- Verify CSRFProtect is initialized in app.py

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Personal Blog project](https://roadmap.sh/projects/personal-blog/solutions?u=692db4d2a17ff74763dc81f1).

---

**Project URL:** https://roadmap.sh/projects/personal-blog/solutions?u=692db4d2a17ff74763dc81f1

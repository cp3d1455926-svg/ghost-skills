# Contributing to Ghost Skills

Thank you for considering contributing to Ghost Skills! 🤝👻

## 🚀 Quick Start

### 1. Fork the Repository

Click the "Fork" button in the top-right corner of GitHub

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/OpenClaw-good-skills.git
cd OpenClaw-good-skills
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## 📝 Commit Message Convention

### Format

```
<type>(<scope>): <subject>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build/config changes

### Examples

```
feat(movie-recommender): add Douban API integration
fix(weather): fix encoding issue on Windows
docs: update README installation steps
refactor(skill-creator): improve error handling
```

## 🛠️ Creating a New Skill

### 1. Use skill-creator (Recommended)

```bash
# In OpenClaw
"Help me create a new skill named xxx"
```

### 2. Manual Creation

```bash
cd skills
mkdir your-skill-name
cd your-skill-name
```

### Required Files

```
your-skill-name/
├── SKILL.md           # Skill description and triggers
├── index.js           # Main logic (or script.py)
├── README.md          # Usage documentation
└── _meta.json         # Optional: Metadata
```

### SKILL.md Template

```markdown
---
name: your-skill-name
description: Brief description of your skill
---

# Your Skill Name

## Core Functionality

Describe what your skill does...

## Usage Examples

```
Example trigger phrases...
```

## Implementation Details

Technical details...
```

## ✅ Before Submitting

### Checklist

- [ ] Read [SKILL.md](SKILL.md) to understand functionality
- [ ] Read [README.md](README.md) for usage instructions
- [ ] Check for suspicious shell commands
- [ ] Verify permission requests are reasonable
- [ ] No hardcoded API keys or credentials
- [ ] Test skill functionality
- [ ] Update documentation if needed

### Testing Your Skill

1. Place skill in `workspace/skills/`
2. Enable skill in OpenClaw
3. Test all functionality
4. Check logs for errors
5. Test edge cases

## 📤 Submitting Changes

### 1. Commit Changes

```bash
git add .
git commit -m "feat: add your-skill-name"
```

### 2. Push to GitHub

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

- Go to your fork on GitHub
- Click "Pull Request"
- Fill in the PR description:
  - What does this PR do?
  - Why is this change needed?
  - How to test this PR?
- Submit PR

## 🔍 Code Review

After submitting a PR:

1. Maintainers will review your code
2. Address any feedback or requested changes
3. Once approved, your PR will be merged

## 💡 Tips

- Keep skills focused on a single purpose
- Follow existing code patterns
- Add comments for complex logic
- Include usage examples in README
- Test thoroughly before submitting

## ❓ Questions?

Feel free to open an issue with the "question" label!

---

**Thanks for contributing! 🎉**

*Made with 👻 by Ghost & Jake*

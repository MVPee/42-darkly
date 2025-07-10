🚨 **EXPLOIT**

The application includes a URL like:
`/?page=redirect&site=melvium.com`

This allows attackers to redirect users to external, potentially malicious websites by manipulating the site parameter. This is known as an **open redirect** vulnerability.

---

✅ **PATCH**

Use static balise tags

```html
<a href="https:/facebook.com" rel="noopener noreferrer" target="_blank"
  >Go to Facebook!</a
>
```

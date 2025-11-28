- tardy.com
- Email workspace gmail
- Images
- 

python3 -m http.server 8000       

Hey Cyril!

Ok, a short note of a few things:

- Can you send me the logins to the current website, and or domain registrator?
- We said you also own "tardy.com" and will see if we can build a website here!
- Will you please send me all the pictures you have?
- I will get some detail about that game, and do a one-pager proposal we can perhaps present to the tourist office
- We will try and get a tardy.com email address (like ski@tardy.com)


- Build for linux/amd64 if uploading to GCP, as GCP does not support arm (default on mac m1)
```
docker build --platform=linux/amd64 --progress=plain -t europe-west9-docker.pkg.dev/tardy-477718/tardy/website:test .
```
- push up to artifact registry
```
docker push europe-west9-docker.pkg.dev/tardy-477718/tardy/website:test
```

us-central1-docker.pkg.dev/buymyitem/tardy


      serviceAccountName: firebase-adminsdk-fbsvc@tardy-477718.iam.gserviceaccount.com



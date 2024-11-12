# Use Disks in Python Platform
## How to deploy? 
```
git clone https://github.com/liara-cloud/python-getting-started.git
```
```
cd python-getting-started
```
```
git checkout diskSetup
```
```
npm install -g @liara/cli
```
```
liara login
```
```
liara create # create python app
liara disk:create # create a disk
```
- modify `liara.json` 
```
liara deploy --platform python --port 8000
```

## More Docs?
- [Liara](https://docs.liara.ir/paas/python/how-tos/use-disk/)

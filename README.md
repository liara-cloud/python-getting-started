# Python apps getting started

Example of how deploy a simple Python project on [liara](https://liara.ir).

## Deploying

[Create New Docker App](https://console.liara.ir/apps/create) & install the [Liara CLI](https://docs.liara.ir/cli/install)

```bash
$ git clone https://github.com/liara-cloud/python-getting-started.git # or clone your own fork

$ cd python-getting-started

```
- create a new disk in your app --> [docs](https://docs.liara.ir/storage/disks/about/)
- change liara.json file in project due to your disk name

```bash
$ liara deploy
```
- check your disk content using FTP Access --> [docs](https://docs.liara.ir/storage/disks/ftp/)

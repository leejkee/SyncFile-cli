# 同步文件的命令行工具
一个使用python实现的命令行工具，将目标目录ResourceDir的文件同步到指定目录DestinationDir

## 脚本会做什么？
会复制全部文件和文件夹，并且跳过已经存在的文件

## 说明

- 同步文件： 从`ResourceDir` 到 `DestinationDir`
- `ResourceDir` 默认为 `~\Pictures\icon`
- `DestinationDir` 默认为 当前目录
- 使用 `-h` 获取帮助 
- 使用 `-t` 测试执行情况
## 使用

### Linux
```bash
python main.py
```

### Windows

```ps1
python.exe .\main.py
```

### 测试模式
如果担心目录有问题，可以先执行测试模式看看文件同步情况
# shimo2png

由于之前做题记录一直写在石墨文档，导出后`markdown`文件后发现插入的图片被转为了`base64`格式，文件大小动辄`2,30M`

简单撸了个jio本将石墨文档导出的`.md`文件中的`base64编码图片`转换为`png`图片

```python
python main.py post.md
```

![image](https://user-images.githubusercontent.com/31686695/158354334-70c74c12-108c-4fa9-bceb-9fec0f2f1453.png)

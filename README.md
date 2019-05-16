# elmo_python
## 一、环境
- 使用python3
- 安装allennlp包，这个包里面包含了Elmo模块

## 二、使用elmo的两种方法
1. 直接下载两个文件在本地，下载地址为：
```
options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"	
weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"
```

  调用代码：
```
options_file = "./elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "./elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"
```

2. 直接在线上导入文件

```
options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"	
weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

```


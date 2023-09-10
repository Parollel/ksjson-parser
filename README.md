# 依赖
该项目的脚本使用 [bash](https://www.gnu.org/software/bash) 编写且需要使用 [jq](https://github.com/jqlang/jq)。  

# 使用方法
在该仓库的根目录下创建一个 `json` 文件夹,  
将使用 [FreeMote](https://github.com/UlyssesWu/FreeMote) 获取的 `.ks.json` 文件放入上一步创建的 `json` 文件夹中。  
运行 `format.sh` 会将 `json` 文件夹中的所有 json 文件格式化并生成 `json.list` 用于记录 `json` 文件夹中包含的文件, 所以在每次加入新文件后请运行一次 `format.sh`。  
如果您是初次运行 `format.sh`, 则还会生成用于放置提取内容的文件夹。  
之后运行 `extract_all.sh`, 会将 `json.list` 记录的所有文件进行提取。  
提取完之后您可以进行修改, 修改完毕之后运行 `apply_all.sh` 可以将修改内容应用到 `json.list` 记录的文件中。  
应用完毕后再使用 [FreeMote](https://github.com/UlyssesWu/FreeMote) 生成 `.scn` 文件。  
**注意**: 因为文件名完全由 `json.list` 记录, 所以请勿随意修改文件名。

### 基础

git init        //初始化 工作区

git add 1.md        // 将1.md添加到缓冲区

git add.            // 将当前目录下所有文件都添加到缓冲区

git commit -m "xxxxx"       //归档

git push origin master      // 将归档的文件上传到仓库

git status              //查看当前本地仓库状态

### 回滚

git log             // 查看git提交历史

git reflog          // 查看操作记录，可以看到回滚前的哈希

git reset --mixed 53a7ca073d92a3f21e3bc53780ba15d02a5be4e9  //将缓冲区和归档区的文件进行回滚

git reset --hard        //恢复已做的更改到指定的版本，包括工作区，缓冲区，归档区

git reset --soft        //只回滚归档区

git revert 53a7ca073d92a3f21e3bc53780ba15d02a5be4e9     //将文件恢复至指定的改动之前的版本

### 多分支操作

git branch -v           //查看当前分支数量

git checkout -b xx          // 切换当前分支到xx分支下

git checkout master         // 切换到master分支下

git merge xx                // 将xx分支合并到master分支

### 添加远程仓库

git remote add [shortname] [url]

### 拉取远程仓库

git pull                // == git fetch + git merge 当本地的落后于线上仓库时，使用此命令

git fetch               //获取到线上仓库的更新

git merge               //合并分支到主干

### VS CODE 连接到Github

1. 安装GIT
2. 终端中输入命令：`git config --global user.name "natlqs"`
3. 终端中输入命令：`git config --global user.email "natlqs@outlook.com"`
4. 终端中输入命令:`$ ssh-keygen -t rsa -C "natlqs@outlook.com`成功的话会在 ~/ 下生成 .ssh 文件夹，进去，打开 id_rsa.pub，复制里面的 key。
5. 回到 github 上，进入 Account => Settings（账户配置）。
6. 左边选择 SSH and GPG keys，然后点击 New SSH key 按钮,title 设置标题，可以随便填，粘贴在你电脑上生成的 key。
7. 为了验证是否成功，输入以下命令：`ssh -T git@github.com$ ssh -T git@github.com The authenticity of host 'github.com (52.74.223.119)' can't be established. RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8. Are you sure you want to continue connecting (yes/no/[fingerprint])? yes                   # 输入 yes Warning: Permanently added 'github.com,52.74.223.119' (RSA) to the list of known hosts. Hi tianqixin! You've successfully authenticated, but GitHub does not provide shell access. # 成功信息 ![](image/git_command/1640910683470.png)`
   以上信息说明验证成功
8.

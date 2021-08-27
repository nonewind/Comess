<!--
 * @Author: Ziheng
 * @Date: 2021-08-27 17:20:14
 * @LastEditTime: 2021-08-27 17:27:46
-->

### Wecom酱 - Python 版本
- [原项目:Wecom酱](https://github.com/easychen/wecomchan)
- [腾讯云函数搭建:腾讯云云函数部署Server酱📣](https://github.com/easychen/wecomchan/tree/main/go-scf)

#### 简单的自我介绍
一开始就很喜欢方糖的的消息提示，无意间看到有腾讯云云函数搭建的方式，就开始按照教程自己撸一个
但是 没有提供Python版本 所以就写了一个Python版本(当然核心代码是原封不动的使用Wecom酱的实例)
#### 依赖说明
- request 需要自己在云函数提供的云编辑器里安装 或者 采用云函数官方的SDK
#### 复刻进度
- [x] 按照原项目文档 已经成功走了一遍
- [ ] 修复无法发送转义字符 \r \n 的问题
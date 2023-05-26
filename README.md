# China-Telecom-ShanDong-IPTV-list

山东电信IPTV直播源

## 更新时间记录

* 2023.5.26
  * 重新整理

## 说明

* 格式说明
  * SD:480P/576P
  * HD:720P
  * FHD:1080P
  * UHD:2160P(4K)
  * FUHD:4320P(8K)

* 文件说明
  * 1.`Cheker-Online-324.m3u8` 通过IPTV-Cheker工具快速筛查，324个频道
  * 2.`VLC-wei.m3u` 使用VLC手动过了一遍，只保留了实际能联通的频道，频道名未整理，包含循环片段频道及广播频道
  * 3.`all(SD+FHD).m3u` 去掉只播放一个片段的频道及广播频道，频道名整理，按频道名字符正序排序，未进行匹配图标及分组
  * 4.`FHD.m3u` & `SD.m3u` 分类，未进行匹配图标及分组
  * 5.`FHD+.m3u` & `SD+.m3u` 通过112114一键匹配台标及分组
  * 6.`External.m3u` 外部资源，UHD+FUHD，已测试秒开
  * 6.`Telecom-Shandong.m3u` 自用，仅UHD及以上，去掉县台及购物台，包含几个 UHD & FUHD 频道，排序

## 资源

* EGP指南数据

| 名称 | 地址 |
|:--------:|:-------------|
| 112114 | `https://epg.112114.xyz/pp.xml` |
| 老张：央视 | `http://epg.51zmt.top:8000/cc.xml` |
| 老张：地方 | `http://epg.51zmt.top:8000/difang.xml` |
| epg.pw | `https://epg.pw/xmltv/epg_CN.xml` |
| bevy.be | `https://www.bevy.be/bevyfiles/chinapremium1.xml` |
| iptv-org | `https://raw.githubusercontent.com/iptv-pro/iptv-pro.github.io/main/epg/epg.xml` |

* EGP工具
  * 1.[WebGrab+Plus](http://webgrabplus.com/download)
  * 2.[老张的EPG开源仓库](https://github.com/supzhang/epg)

* 播放工具
  * 1.Windows：[Potplayer](http://potplayer.tv/)
  * 2.Mac：[IINA](https://www.iina.io/)
  * 3.Services：[Emby](https://emby.media/)

## 播放列表中属性的说明

* M3U结构
  * tvg-id - EPG代码表中的频道代码
  * tvg-name - EPG代码表中的频道名称
  * group-title - 频道组名
  * parent-code - 组的父代码
  * audio-track - ISO 639-1 音轨代码 (仅限LG, [查看代码表](http://www.loc.gov/standards/iso639-2/php/code_list.php))
  * tvg-logo - 大的频道徽标的路径，最小高度应为 48px
  * tvg-logo-small - 小的方形频道徽标的路径，最小高度应为 48px（仅适用于最新的应用程序版本）
  * timeshift, tvg-rec - 特定频道的时移可用性
  * 示例：
  
    ```txt
    #EXTM3U
    #EXTINF:-1 tvg-id="Be1.be" tvg-name="Be1 Alt" group-title="News" parent-code="1234" audio-track="nl",Be1 Name
    <http://channel.stream.address/to_be_placed/on_separate_line/123.ts>
    ```

* TXT 结构（旧方法，不推荐）
  
  ```txt
  group,Common,1234
  EPGcode,Channel Name,<http://channel.stream.address,en,1>
  avi,Video File,<http://video.file.address.mkv>
  ```

  * 在 EPG 代码页面上，您将找到要添加的 EPG 代码列表，而不是“EPGcode”，或者如果没有可用于特定频道的 EPG 代码，则输入“ext”。频道名称后的“en”表示首选音轨（适用于 LG 电视）。行尾的“1”表示此特定通道上有可用的时移。“avi”用于视频文件和其他视频资源（Youtube，Vkontakte）。组名称后的“1234”设置整个组的家长代码。

* 网络 视频/音频 播放
  * 在TXT列表中的示例
  
  ```txt
  avi,Video pro Zajchika,<http://www.quirksmode.org/html5/videos/big_buck_bunny.mp4>
  avi,Music 1,<http://siptv.eu/temp/malandra.mp3>
  ```

## 交流

QQ群：757694351

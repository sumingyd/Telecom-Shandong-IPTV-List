# China-Telecom-ShanDong-IPTV-list
山东电信IPTV直播源

# 更新时间记录：
- 2023.1
- 未来将仅保留1080P及以上分辨率的频道。

# EGP指南数据：
- 1.[Diyp](http://epg.51zmt.top:8000/)
- 2.[百川](https://epg.112114.eu.org/)

# 直播工具：
- 1.Windows：[Potplayer](http://potplayer.tv/)
- 2.Mac：[IINA](https://www.iina.io/)
- 3.Services：[Emby](https://emby.media/)

# 播放列表中属性的说明

1. M3U结构：
- tvg-id - EPG代码表中的频道代码
- tvg-name - EPG代码表中的频道名称
- group-title - 频道组名
- parent-code - 组的父代码
- audio-track - ISO 639-1 音轨代码 (仅限LG, [查看代码表](http://www.loc.gov/standards/iso639-2/php/code_list.php))
- tvg-logo - 大的频道徽标的路径，最小高度应为 48px
- tvg-logo-small - 小的方形频道徽标的路径，最小高度应为 48px（仅适用于最新的应用程序版本）
- timeshift, tvg-rec - 特定频道的时移可用性
- 示例：
- #EXTM3U
- #EXTINF:-1 tvg-id="Be1.be" tvg-name="Be1 Alt" group-title="News" parent-code="1234" audio-track="nl",Be1 Name
- http://channel.stream.address/to_be_placed/on_separate_line/123.ts

2. TXT 结构（旧方法，不推荐）
- group,Common,1234
- EPGcode,Channel Name,http://channel.stream.address,en,1
- avi,Video File,http://video.file.address.mkv
- 在 EPG 代码页面上，您将找到要添加的 EPG 代码列表，而不是“EPGcode”，或者如果没有可用于特定频道的 EPG 代码，则输入“ext”。频道名称后的“en”表示首选音轨（适用于 LG 电视）。行尾的“1”表示此特定通道上有可用的时移。“avi”用于视频文件和其他视频资源（Youtube，Vkontakte）。组名称后的“1234”设置整个组的家长代码。

# 网络 视频/音频 播放

1. 在TXT列表中的示例：
- avi,Video pro Zajchika,http://www.quirksmode.org/html5/videos/big_buck_bunny.mp4
- avi,Music 1,http://siptv.eu/temp/malandra.mp3

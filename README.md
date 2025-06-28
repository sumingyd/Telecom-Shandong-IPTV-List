# China-Telecom-ShanDong-IPTV-list

山东电信IPTV直播源

## 更新日志
**2025年5月22日**  
本次更新包含以下优化：

新增广东卫视-4K
新增深圳卫视-4K

## 说明

* 格式说明
  * SD:480P/576P
  * HD:720P
  * FHD:1080P
  * UHD:2160P(4K)
  * FUHD:4320P(8K)

* 文件说明
  * 1.`External.m3u` 外部资源，UHD+FUHD，已测试秒开
  * 2.`Telecom-Shandong.m3u` 自用，仅FHD及以上，去掉县台及购物台
  * 3.`对应表.xlsx`每次更新方便的，可无视。
  * 4.`Unicom-Shandong.m3u` 仅限山东联通使用。
  * 6.`bak` 备份目录（之前更新过的文件，但不想再更新了，可用）
  * 7.`img` 台标目录
  * 8.`Telecom-Jiangsu-Multicast.m3u` 仅限江苏组播使用。
  * 9.`Telecom-Shandong-Multicast.m3u` 自用，仅FHD及以上。
  * 10.`Telecom-Shandong-Multicast-SD.m3u` 仅SD及以下。

## 资源

* EGP指南数据

| 名称 | 地址 |
|:--------:|:-------------|
| 112114 | 主用：`https://raw.githubusercontent.com/sparkssssssssss/epg/main/pp.xml` 备用：`https://epg.112114.xyz/pp.xml` |
| 老张：总表 | `http://epg.51zmt.top:8000/e.xml` |
| 老张：央视 | `http://epg.51zmt.top:8000/cc.xml` |
| 老张：地方 | `http://epg.51zmt.top:8000/difang.xml` |
| fanmingming | `https://live.fanmingming.com/e.xml` |
| epg.pw：总表 | `https://epg.pw/xmltv/epg.xml` |
| epg.pw：中国 | `https://epg.pw/xmltv/epg_CN.xml` |
| bevy.be | `https://www.bevy.be/bevyfiles/chinapremium1.xml` |
| iptv-org | `https://raw.githubusercontent.com/iptv-pro/iptv-pro.github.io/main/epg/epg.xml` |

* EGP工具
  * 1.[WebGrab+Plus](http://webgrabplus.com/download)  根据编写的规则采集设定的节目表，自定义频道名称及频道代码
  * 2.[老张的EPG开源仓库](https://github.com/supzhang/epg)

* 播放工具
  * 1.Windows：[Potplayer](http://potplayer.tv/)
  * 2.Mac：[IINA](https://www.iina.io/)
  * 3.Services：[Emby](https://emby.media/)

## 播放列表中属性的说明

* M3U结构

| 属性名称 | 解释 |
|:--------:|:-------------|
| tvg-id | 频道唯一ID |
| tvg-name | 频道名称 |
| group-title | 频道组名 |
| tvg-chno | 频道号 |
| parent-code | 组的父代码 |
| tvg-country | 国家 |
| tvg-language | 语言 |
| audio-track | ISO 639-1 音轨代码 (仅限LG, [查看代码表](http://www.loc.gov/standards/iso639-2/php/code_list.php)) |
| tvg-logo | 标准频道徽标，最小高度应为 48px |
| tvg-logo-small | 小的方形频道徽标，最小高度应为 48px（仅适用于最新的应用程序版本） |
| tvg-shift | 更换EPG的小时数 (仅在需要时使用) |
| timeshift, tvg-rec | 特定频道的时移可用性 |

* 示例：

    ```txt
    #EXTM3U
    #EXTINF:-1 tvg-id="Be1.be" tvg-name="Be1 Alt" group-title="News" parent-code="1234" audio-track="nl",Be1 Name
    http://channel.stream.address/to_be_placed/on_separate_line/123.ts
    ```

* TXT 结构（旧方法，不推荐）
  
  ```txt
  group,Common,1234
  EPGcode,Channel Name,http://channel.stream.address,en,1
  avi,Video File,http://video.file.address.mkv
  ```

  * 在 EPG 代码页面上，您将找到要添加的 EPG 代码列表，而不是“EPGcode”，或者如果没有可用于特定频道的 EPG 代码，则输入“ext”。频道名称后的“en”表示首选音轨（适用于 LG 电视）。行尾的“1”表示此特定通道上有可用的时移。“avi”用于视频文件和其他视频资源（Youtube，Vkontakte）。组名称后的“1234”设置整个组的家长代码。

* 网络 视频/音频 播放
  * 在TXT列表中的示例
  
  ```txt
  avi,Video pro Zajchika,http://www.quirksmode.org/html5/videos/big_buck_bunny.mp4
  avi,Music 1,http://siptv.eu/temp/malandra.mp3
  ```

## 频道时移说明

* 如果你是IPTV/OTT提供商，你可以通过以下方式实现存档节目支持:

  * 在你的M3U播放列表中包含timshift="1"属性，以添加对特定频道的时移支持，其中1是该频道可用的时移天数。

  * 使用添加到流URL中的Unix时间格式参数(以秒为单位)组织频道流上的时间提示。例如:`http://our.stream.url:8080/some_stream_info/?utc=1425988050& utc=1425988225`，其中utc=1425988050是星期二，2015年3月10日11:47:30 GMT的日期，当用户选择一些特定的程序使用EPG列表为当前的一天或过去的一天(最多15天)，这是由应用程序自动添加到URL的。另外，URL中还添加了另一个可选参数lutc=1425988225，用于指定当前时间。

  * 您可以通过将完整的归档流URL加载到VLC应用程序来检查归档编程的功能，该应用程序应该在特定的时间提示开始。
    * 使用[Epoch转换器](https://www.epochconverter.com/)找到必要的Unix时间。

  * 如果你有一些特定的timeeshift URL配置为你的流，你可以通过基于服务器的脚本做必要的调整，以便当你从应用程序请求的URL中收到"utc="提示点时，输出必要的URL结构。

## 交流

QQ群：757694351

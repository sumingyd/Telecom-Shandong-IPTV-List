# 山东电信IPTV直播源

[![GitHub stars](https://img.shields.io/github/stars/sumingyd/Telecom-Shandong-IPTV-List?style=flat-square)](https://github.com/sumingyd/Telecom-Shandong-IPTV-List/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sumingyd/Telecom-Shandong-IPTV-List?style=flat-square)](https://github.com/sumingyd/Telecom-Shandong-IPTV-List/network)
[![GitHub issues](https://img.shields.io/github/issues/sumingyd/Telecom-Shandong-IPTV-List?style=flat-square)](https://github.com/sumingyd/Telecom-Shandong-IPTV-List/issues)
[![GitHub license](https://img.shields.io/github/license/sumingyd/Telecom-Shandong-IPTV-List?style=flat-square)](https://github.com/sumingyd/Telecom-Shandong-IPTV-List/blob/main/LICENSE)

一个收集和整理山东电信IPTV直播源的项目，提供高质量的直播源文件和播放列表。

## 📋 项目简介

本项目致力于收集和维护山东电信IPTV的直播源，包括高清、标清和4K频道，为IPTV爱好者和开发者提供稳定可靠的直播源文件。

## 🚀 快速开始

### 文件说明

| 文件名称 | 描述 | 适用场景 |
|---------|------|----------|
| `Telecom-Shandong.m3u` | 山东电信单播 | 完整列表 |
| `Telecom-Shandong-Multicast.m3u` | 山东电信组播 | 完整列表 |
| `Telecom-Jiangsu-Multicast.m3u` | 江苏组播列表 | 群友贡献 |
| `Unicom-Shandong-Multicast.m3u` | 山东联通组播 | 群友贡献 |
| `Unicom-Shandong.m3u` | 山东联通单播 | 群友贡献 |
| `Mobile-Shandong.m3u` | 山东移动单播 | 群友贡献 |
| `联通组播地市级` | `济南 242``泰安 240``德州 250``济宁 244``威海 230``菏泽 236``烟台 248``潍坊 246``莱芜 222``滨州 234``聊城 228``日照 224``淄博 252``东营 232``青岛 254``枣庄 226 | 每个城市第三段IP不同，可自行替换 |
| `img/` | 台标资源 | 目前列表内使用的是扫描器仓库内的台标，此文件夹仅作保留，不再更新 |

## 📺 播放列表使用

### 支持的播放器

- **Windows**: [PotPlayer](http://potplayer.tv/)
- **macOS**: [IINA](https://www.iina.io/)
- **Linux**: VLC Media Player
- **服务端**: [Emby](https://emby.media/), Plex, Jellyfin
- **Android**: 酷9

### 使用方法

1. 下载所需的 `.m3u` 文件
2. 在支持的播放器中打开文件
3. 选择想要观看的频道

## 📊 EPG电子节目指南

### 推荐EPG源

| 提供商 | 地址 | 特点 |
|--------|------|------|
| 时光轨车 | `https://raw.githubusercontent.com/sggc/SD-EPG/refs/heads/main/EPG/sggc-desc.xml.gz` | 适配本整理源并适配本源的县级频道，含desc节目描述 |
| 老张EPG | `http://epg.51zmt.top:8000/e.xml.gz` | 老张 |
| epg.pw | `https://epg.pw/xmltv/epg_CN.xml` | 中国频道专用 |

### EPG工具

- **[WebGrab+Plus](http://webgrabplus.com/download)**: 自定义节目表采集工具
- **[老张EPG仓库](https://github.com/supzhang/epg)**: 开源EPG项目

## 🔧 技术说明

### M3U播放列表IPTV属性标签

| 标签名称 | 含义说明 | 示例值 |
|---------|----------|--------|
| **`tvg-id`** | 频道在EPG数据源中的唯一标识符，用于匹配节目指南 | `tvg-id="CCTV1.cn"` |
| **`tvg-name`** | 频道名称，当`tvg-id`不可用时作为备用匹配项 | `tvg-name="中央电视台综合频道"` |
| **`tvg-logo`** | 频道台标的URL地址或本地文件路径 | `tvg-logo="https://example.com/logo/cctv1.png"` |
| **`tvg-chno`** | 频道号码，用于在播放器中自定义频道排序 | `tvg-chno="1"` |
| **`group-title`** | 频道分组名称，多个分组用分号分隔 | `group-title="中央台;高清"` |
| **`tvg-language`** | 频道的主要语言 | `tvg-language="Chinese"` |
| **`tvg-country`** | 频道所属的国家或地区 | `tvg-country="China"` |
| **`tvg-shift`** | EPG时间的时区偏移量（小时），用于时间校正 | `tvg-shift="-1"` |
| **`tvg-timezone`** | 为特定频道指定时区，覆盖全局设置 | `tvg-timezone="Asia/Shanghai"` |
| **`catchup`** | 启用回看功能 | `catchup="default"` |
| **`catchup-days`** | 回看功能可获取过去多少天的节目 | `catchup-days="7"` |
| **`catchup-source`** | 回看流的URL模板，包含时间戳占位符 | `catchup-source="https://example.com/playlist?start={utc}"` |
| **`timeshift`** | 直播流的时移缓冲时间（秒） | `timeshift="10800"` |
| **`url-tvg`** | 指定EPG源（XMLTV格式）的URL | `url-tvg="https://example.com/epg.xml"` |
| **`aspect-ratio`** | 建议播放器使用的视频宽高比 | `aspect-ratio="16:9"` |
| **`geo-auth`** | 指定该频道或流是否有地域限制 | `geo-auth="yes"` |

### 示例格式

```m3u
#EXTM3U
#EXTINF:-1 tvg-id="CCTV1.cn" tvg-name="CCTV1" tvg-logo="https://example.com/cctv1.png" tvg-chno="1" group-title="新闻;综合" tvg-language="zh" tvg-country="CN" tvg-shift="0" catchup="default" catchup-days="7" catchup-source="http://example.com/{utc}",CCTV-1 综合
http://example.com/stream/live/cctv1
```

## 🛠️ 工具推荐

### 扫描工具

- **[IPTV-Scanner-Editor-Pro](https://github.com/sumingyd/IPTV-Scanner-Editor-Pro)**: 专业的IPTV扫描编辑工具

### 测试工具

- **VLC Media Player**: 用于测试流媒体链接
- **ffmpeg**: 命令行流媒体测试工具

## 📞 交流群组

- **QQ群**: 757694351
- 欢迎加入交流IPTV相关技术和资源

## ⚠️ 免责声明

本项目仅用于学习和研究目的，请勿用于商业用途。所有直播源均来自网络，版权归相关电视台所有。请在24小时内删除下载的内容。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

**如果这个项目对您有帮助，请给个⭐Star支持一下！**

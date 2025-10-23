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
| `Telecom-Shandong.m3u` | 单播播放列表 | 完整列表 |
| `Telecom-Shandong-Multicast.m3u` | 组播播放列表 | 完整列表 |
| `Telecom-Jiangsu-Multicast.m3u` | 江苏组播列表 | 群友贡献 |
| `External.m3u` | 外部资源 | UHD+FUHD画质，已测试秒开 |
| `扫描/` | 扫描数据 | 包含组播标清和高清的扫描数据表格 |
| `img/` | 台标资源 | 所有频道的台标图片 |
| `bak/` | 备份文件 | 历史版本的播放列表备份 |

### 画质说明

- **SD**: 480P/576P (标清)
- **HD**: 720P (高清)
- **FHD**: 1080P (全高清)
- **UHD**: 2160P (4K超高清)
- **FUHD**: 4320P (8K超高清)

## 📺 播放列表使用

### 支持的播放器

- **Windows**: [PotPlayer](http://potplayer.tv/)
- **macOS**: [IINA](https://www.iina.io/)
- **Linux**: VLC Media Player
- **服务端**: [Emby](https://emby.media/), Plex, Jellyfin

### 使用方法

1. 下载所需的 `.m3u` 文件
2. 在支持的播放器中打开文件
3. 选择想要观看的频道

## 📊 EPG电子节目指南

### 推荐EPG源

| 提供商 | 地址 | 特点 |
|--------|------|------|
| 112114 | `https://raw.githubusercontent.com/springs/epg/main/pp.xml` | 主用源，更新及时 |
| 老张EPG | `http://epg.51zmt.top:8000/e.xml` | 总表，频道全面 |
| fanmingming | `https://live.fanmingming.com/e.xml` | 简洁高效 |
| epg.pw | `https://epg.pw/xmltv/epg_CN.xml` | 中国频道专用 |

### EPG工具

- **[WebGrab+Plus](http://webgrabplus.com/download)**: 自定义节目表采集工具
- **[老张EPG仓库](https://github.com/supzhang/epg)**: 开源EPG项目

## 🔧 技术说明

### M3U播放列表结构

播放列表遵循标准M3U格式，包含以下属性：

| 属性 | 说明 |
|------|------|
| `tvg-id` | 频道唯一标识符 |
| `tvg-name` | 频道名称 |
| `group-title` | 频道分组 |
| `tvg-chno` | 频道编号 |
| `tvg-logo` | 频道台标URL |
| `tvg-country` | 国家代码 |
| `tvg-language` | 语言代码 |
| `audio-track` | 音轨代码 (ISO 639-1) |

### 示例格式

```m3u
#EXTM3U
#EXTINF:-1 tvg-id="CCTV1" tvg-name="CCTV-1综合" group-title="央视" tvg-logo="https://example.com/cctv1.png",CCTV-1综合
http://example.com/stream/cctv1.m3u8
```

## 🛠️ 工具推荐

### 扫描工具

- **[IPTV-Scanner-Editor-Pro](https://github.com/sumingyd/IPTV-Scanner-Editor-Pro)**: 专业的IPTV扫描编辑工具

### 测试工具

- **VLC Media Player**: 用于测试流媒体链接
- **ffmpeg**: 命令行流媒体测试工具

## 📝 更新日志

### 2025年9月28日
- ✅ 移除部分失效频道
- ✅ 增加多个4K频道
- ✅ 为部分频道增加高清版本
- ✅ 优化播放列表结构

## 🤝 贡献指南

欢迎提交Issue和Pull Request来帮助改进这个项目：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个Pull Request

## 📞 交流群组

- **QQ群**: 757694351
- 欢迎加入交流IPTV相关技术和资源

## ⚠️ 免责声明

本项目仅用于学习和研究目的，请勿用于商业用途。所有直播源均来自网络，版权归相关电视台所有。请在24小时内删除下载的内容。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

**如果这个项目对您有帮助，请给个⭐Star支持一下！**

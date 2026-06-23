# Agnes AI

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README.zh-CN.md">简体中文</a>
</p>

Agnes AI 官方 API 网关与模型目录。

Agnes AI 通过统一的 API 网关，为开发者提供 OpenAI 兼容的多模态模型访问能力，覆盖文本、图像、视频和 Agent 工作流。

## 文档状态

| 字段 | 值 |
| --- | --- |
| 公共文档版本 | `2026.06.22` |
| 最后更新 | `2026-06-22 00:00 Asia/Singapore` |
| 信息来源 | 官方网站与 API 平台 |
| 变更说明 | 模型可用性、速率限制、价格和配额规则可能随时间变化。生产环境使用前，请以官方文档或平台控制台为准。 |

## 快速链接

| 资源 | URL |
| --- | --- |
| 官网 | https://agnes-ai.com/ |
| 开发者文档 | https://agnes-ai.com/doc/overview |
| API 平台 | https://platform.agnes-ai.com/ |
| API Base URL | `https://apihub.agnes-ai.com/v1` |

## 开发者资源

| 资源 | 用途 |
| --- | --- |
| [`MODEL_CATALOG.md`](./MODEL_CATALOG.md) | 模型系列、端点、当前参考限制和兼容性说明。 |
| [`CHANGELOG.md`](./CHANGELOG.md) | 公共文档、模型、配额和集成变更记录。 |
| [`SUPPORT.md`](./SUPPORT.md) | 如何获取帮助，哪些内容适合提交到 issues 或 discussions。 |
| [`docs/TROUBLESHOOTING.md`](./docs/TROUBLESHOOTING.md) | API 错误码、排查清单和重试建议。 |
| [`docs/FAQ.md`](./docs/FAQ.md) | 关于访问权限、限制、模型和视频轮询的常见问题。 |
| [`docs/DISCUSSIONS.md`](./docs/DISCUSSIONS.md) | 推荐的讨论分类和社区协作流程。 |
| [`examples/`](./examples) | 最小化 curl、Python 和 Node.js 示例。 |

## 模型

| 模型 | 类型 | 端点 | 亮点 |
| --- | --- | --- | --- |
| `agnes-2.0-flash` | 文本与视觉语言 | `/v1/chat/completions` | 推理、代码、工具调用、流式输出、图像理解和 Agent 工作流 |
| `agnes-image-2.0-flash` | 图像生成与编辑 | `/v1/images/generations` | 文生图、图生图、URL 或 Base64 输出 |
| `agnes-image-2.1-flash` | 图像生成与编辑 | `/v1/images/generations` | 高密度视觉生成、图像编辑、灵活尺寸、URL 或 Base64 输出 |
| `agnes-video-v2.0` | 视频生成 | `/v1/videos` | 文生视频、图生视频、多图视频、关键帧动画、异步任务 API |

## 当前访问与限制

以下数值是截至 `2026-06-22` 的公开参考值，属于运行限制，不是永久承诺。

### 用户计划

| 用户计划 | 文本模型 RPM | 图像模型配额 | 视频模型配额 |
| --- | ---: | --- | --- |
| Free / default | 20 actual RPM | 按分辨率适用不同 RPM 限制 | 20 actual RPM |
| Enterprise | 40 actual RPM | 更高的分辨率相关 RPM 限制 | 40 actual RPM |
| Token Plan | 文本模型 1,000 actual RPM | 1K 和 2K 图像具备更高 RPM 限制 | 100 actual RPM |

### 订阅配额

| 计划 | `agnes-2.0-flash` | `agnes-image-2.0/2.1-flash` | `agnes-video-v2.0` |
| --- | --- | --- | --- |
| Starter | 每 5 小时 1,500 次请求；每周 15,000 次请求 | 每天 4,000 张图片 | 每天 500 秒 |
| Plus | 每 5 小时 7,500 次请求；每周 75,000 次请求 | 每天 4,000 张图片 | 每天 500 秒 |
| Pro | 每 5 小时 30,000 次请求；每周 300,000 次请求 | 每天 4,000 张图片 | 每天 500 秒 |

详细的模型级 RPM 表请查看 [`MODEL_CATALOG.md`](./MODEL_CATALOG.md)。

## Chat 示例

```bash
curl https://apihub.agnes-ai.com/v1/chat/completions \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-2.0-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain how to integrate an OpenAI-compatible API gateway."
      }
    ],
    "stream": true
  }'
```

## Image 示例

```bash
curl https://apihub.agnes-ai.com/v1/images/generations \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-image-2.1-flash",
    "prompt": "A luminous floating city above a misty canyon at sunrise, cinematic realism",
    "size": "1024x768"
  }'
```

## Video 示例

```bash
curl -X POST https://apihub.agnes-ai.com/v1/videos \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-video-v2.0",
    "prompt": "A cinematic shot of a cat walking on the beach at sunset, soft ocean waves, warm golden lighting, realistic motion",
    "height": 768,
    "width": 1152,
    "num_frames": 121,
    "frame_rate": 24
  }'
```

视频生成是异步流程。请先创建任务，再使用返回的 `video_id` 查询结果。

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

当前视频结果查询请使用 `video_id`。除非特定旧流程明确要求，否则不要使用 `task_id`。

## 常见集成说明

- 每次请求都需要使用 `Authorization: Bearer YOUR_API_KEY`。
- API Key 应保存在服务端环境变量中，不要暴露在客户端代码或公开仓库里。
- `agnes-2.0-flash` 当前支持 `256K` 上下文窗口和 `64K` 最大输出参考限制，这是 2026 年 6 月从临时 `1M` 上下文窗口回滚后的状态。
- Thinking mode、流式输出、工具调用和视觉输入可用于兼容的 chat 工作流。生产环境启用高级参数前，请先查看对应模型文档。
- 如遇 `400` 响应，请检查必填参数、请求体结构、图片 URL 可访问性和 response format 的位置。
- 如遇 `401` 响应，请检查 API Key、Bearer token 格式、账号状态和环境变量加载。
- 如遇 `429` 响应，请降低并发，加入带退避的重试，并检查当前计划级 RPM 限制。
- 如遇 `500`、`502`、`503` 或 `520` 响应，请使用指数退避重试，并检查请求 payload 是否可以简化。

## 安全

不要提交 API Key、token、`.env` 文件、包含密钥的截图或私有客户数据。

本地开发时建议使用环境变量：

```bash
export AGNES_API_KEY="your_api_key_here"
```

## 文档

模型参数、响应格式、价格、限制和排查说明，请查看官方文档：

- https://agnes-ai.com/doc/overview
- https://agnes-ai.com/doc/agnes-20-flash
- https://agnes-ai.com/doc/agnes-image-20-flash
- https://agnes-ai.com/doc/agnes-image-21-flash
- https://agnes-ai.com/doc/agnes-video-v20

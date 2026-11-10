# 码到共享优惠码库

这个公开 JSON 文件供所有已安装「码到」的 iPhone 读取。打开 Uber、Uber Eats 或 Waymo 时，App 只读取这里已整理的候选码，不现场搜索。

## 数据来源

正式优惠码仅收录从用户手机上的「点点 App」搜索结果中人工核对过的代码。当前还没有收到点点 App 的搜索结果，因此 `codes.json` 中没有正式优惠码。不能用点点开发平台的模型回答、普通网页搜索或猜测的代码代替点点 App 搜索结果。

## 临时测试记录

用户要求测试同步与通知，因此库中暂时加入了三条 `TEST-` 假码。它们的 `is_test` 为 `true`，标题和使用条件均注明不可兑换，48 小时后过期。它们不是点点 App 搜索结果。`source` 暂填 `dots_app` 仅为了让已经安装的旧版 App 读取；不能据此把它们当作真实优惠码。测试结束后会移除。

每条记录格式：

```json
{
  "service": "waymo",
  "code": "EXAMPLE123",
  "source": "dots_app",
  "source_title": "点点 App 搜索结果中的原文标题",
  "source_url": "https://example.com/source",
  "observed_at": "2026-11-10T00:00:00Z",
  "expires_at": null,
  "eligibility": "仅限新用户，或留空"
}
```

`service` 只接受 `uberRide`、`uberEats`、`waymo`。`source_url` 和 `expires_at` 可以为 `null`。`observed_at` 是从点点 App 读取结果的时间，不代表优惠码已通过结账验证。App 会过滤过期或超过七天未复核的记录。

提交新记录前运行 `python3 validate.py`。公开仓库不存储点点 API Key、个人账号、设备数据或点点回答全文。

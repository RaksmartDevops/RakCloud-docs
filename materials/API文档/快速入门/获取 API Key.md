# 获取 API Key

API Key 是调用 RakSmart Cloud API 的身份凭证。所有 API 请求都必须携带有效的 API Key。账户注册完成后，即可在控制台查看您的 API Key。

## 查看步骤

1. 登录 RakSmart 控制台。
2. 单击页面右上角的头像。
3. 在 **Other** 分组中，单击 **API Key**。
4. 页面将显示您的 API Key，复制后即可用于调用 API。

## API Key 格式

API Key 以 `rpk_` 开头，后接 26 位大写字母和数字，例如：

```
rpk_01JH5J3SQ81234567890123456
```

::: danger 安全提示
API Key 拥有操作您账户下全部资源的权限，请妥善保管，勿泄露给他人，也不要在网页、移动应用或公开的代码仓库中使用。如果怀疑 API Key 已经泄露，请立即联系管理员处理。更多建议请参见 [安全最佳实践](../authentication/best-practices.md)。
:::

## 下一步

- [发起第一次调用](./first-request.md)

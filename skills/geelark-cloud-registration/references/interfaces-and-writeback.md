# 连接服务与回填原行

这里记录已验证的接口差异。执行时仍发现当前 schema 和 `--help`，不复制旧完整命令目录。

## 运行配置

| 配置 | 来源/用途 |
| --- | --- |
| `GEELARK_BASE_URL`、`GEELARK_API_KEY` | 本批 GeeLark API；变量名可按部署实际映射 |
| `INHOUSE_BASE_URL`、`INHOUSE_ACCESS_KEY` | 资料库及其 `/api/inhouse-agent-guide` |
| `FEISHU_APPID`、`FEISHU_APPSECRET` 或既有 CLI 授权 | 按当前身份接入飞书 |
| SOP URL、Base token、table ID、原行 ID | 本批私有任务配置，从用户指定来源读取 |
| Cloud `environmentConfigId` | 当前可运行云配置的发现结果 |

环境变量名不是凭据就绪证据。核实当前实例中需要的配置已生效，再用正常客户端测试对应服务。新云会话不会自动获得本机文件或本地技能安装。

## GeeLark 与 ADB

云手机接口使用本批配置的 `/open/v1/` 根路径、Bearer 身份及当前官方要求的请求头。返回 `code=0` 才表示接口成功，仍要核对返回的每台设备结果。参考[官方接口文档](https://github.com/GeeLark/geelark-openapi)。

| 已验证接口 | 请求要点 | 验收 |
| --- | --- | --- |
| `phone/list` | 分页，读取本批 ID | `serialNo` 是编号，`serialName` 是完整名称；`id` 用于后续调用 |
| `phone/start`、`phone/stop` | `{"ids":["<phone_id>"]}` | start 成功后等待运行状态；stop 后回读关机 |
| `shell/execute` | `{"id":"<phone_id>","cmd":"<shell command>"}` | 官方 HTTPS Android shell；读取内层执行状态与 `output` |
| `adb/setStatus`、`adb/getData` | 本批设备 IDs；按实时文档开启和查询连接 | 连接信息与临时连接码只用于本次设备控制 |

已观察的状态：`status=0` 运行、`1` 启动中、`2` 关机；`rpaStatus=0` 是一个空闲信号，仍需核对本批台账与其他操作者。启动期间 `42002 / phone is not running` 不代表长期不可控，应等状态就绪。

用 ADB 或官方 HTTPS shell 启动应用、读取 UI hierarchy、截图和按观测坐标操作。截图可通过 `screencap` 生成后传回；Base64 图片在本地解码，不打印图片内容。对用户电脑上的浏览器/原生应用操作使用当前允许的工具，手机 shell 不能代替桌面权限。

### Museon 设备租约

部署启用 Museon 租约清扫时，直接 GeeLark token 开机或 shell 不会续 Museon 租约。协调器用已有 Museon 身份调用 `POST /admin/cloud-phones/keepalive`，请求包含 `provider_device_id`，交接前续租，操作和用户手动接管期间按现有协议续期，直到关机。

不要为了某批任务停掉全局清扫器。续期接口成功仅证明请求被接受；若仍意外关机，应核对真实租约、清扫日志与设备 ID，不能把其他批次关机日志归因到本批。

## 资料库

先读本批 `INHOUSE_BASE_URL` 的 `/api/inhouse-agent-guide`，再按当前 API 领取、绑定及完成资料。绑定写入后读回相同设备和资料 ID。历史实现中 `completed=true` 会自动清空 `in_use_device`，不应仅据空绑定判断资料又可领取。

默认 Python User-Agent 曾触发资料库 `403 / 1010`，同请求用 `Mozilla/5.0` 成功；这与代理连接阶段 `Tunnel connection failed: 403 Forbidden` 不同。保留既有代理、证书验证和访问规则，先识别拒绝层级。

## 飞书记录

先读当前 `lark-cli base --help` 与所需子命令帮助。旧 `bitable/v1` 与新 `base/v3` scope 不同；旧接口 `99991672` 不能推出整个 Base 无权限。当前 CLI 的 `ok=true` 与底层 API `code=0` 是不同层的成功标记。

原四行按 `record_id` 更新。已验证 `base +record-upsert --record-id` 接收顶层字段 map，不能误包成另一层 `fields`；具体参数仍按当前帮助。一次查询/分页取得本批需要的字段，避免逐行回源拼接；凭据仅在执行者私有内存使用。

| 结果 | 原行字段与证据 |
| --- | --- |
| 通过 | 实际 `username`、HTTPS `profile_link`、业务时区 `login_date`、`is_logged_in=true`、`discarded=false`；更新当前原因字段，历史阻塞保留在备注，资料缺项另记 |
| 人工验证 / 强制手机 / 封禁 | 按本批 SOP：`is_logged_in=false`、`discarded=true`，具体原因及阶段分开记录 |
| 技术未解决 / 待核验 | 两项 false，保留已完成步骤、具体响应、剩余项，不抹去原凭据 |
| 已有成功平台 | 其他平台重试时保持其已验证结果，不重新注册或改写密码 |

历史原表 `discard_reason` 为 URL 类型，应填带说明标题的有效 HTTPS 平台链接，例如 `[需要图片验证码](https://www.instagram.com/)`，而非纯中文被转换成无效 `http://`。过程备注曾使用现有字段 `身份不完整时`；新表先核实真实字段名和类型，不自行照抄新增字段。

执行者更新后读回原行，逐项核对字段和值。登录视图可能过滤掉已成功或弃用行，汇总必须从完整原表取数。

`discarded` 是原表运营状态，不能解释为删除外部平台账号。接续成功时同时核对登录与弃用标记，避免二者都为 true。

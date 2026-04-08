import pytest
import uiautomator2 as u2

# @pytest.fixture(autouse=True, scope="function")
# def start_app():
#     d = u2.connect("22d611e0")  # 连接设备（确保设备序列号正确）
#
#     # 修复1：启动APP逻辑（原else分支缺少click()，且选择器不完整）
#     app = d(text="腾讯爱趣听")
#     if app.exists:
#         app.click()
#     else:
#         # 原代码：d(resourceId="com.iauto.launcher:id/exapp",) → 缺少click()且选择器不完整
#         d(resourceId="com.iauto.launcher:id/exapp").click()  # 补充click()，定位"应用抽屉"
#         d(text="腾讯爱趣听").click()  # 再次尝试点击APP（确保定位到目标）
#
#     yield d  # 返回设备对象给测试函数
#
#     # 修复2：确保包名正确（停止APP时需用正确的包名，避免报错导致fixture异常）
#     d.app_stop("com.tencent.wecarflow")  # 需确认APP的实际包名是否正确
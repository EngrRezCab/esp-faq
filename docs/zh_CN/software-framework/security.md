# 安全

<style>
body {counter-reset: h2}
  h2 {counter-reset: h3}
  h2:before {counter-increment: h2; content: counter(h2) ". "}
  h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
  h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
</style>

---

## ESP8266 的固件是否能被读取？

ESP8266 固件由于放置在外部 flash, 数据可被外部读取。并且 ESP8266 不支持 flash 加密，所有数据均为明文。

---

## 开启 security boot 后, 编译报错缺少文件 ？

> 错误 log: /d/ESP32/esp-mdf/esp-idf/components/bootloader_support/Makefile.projbuild:7：/f/ESP32Root/secure_boot_signing_key.pem

- 报错原因 security boot 是固件签名校验的功能，该功能需要生成证书对。
- 相关资料[参考](https://blog.csdn.net/espressif/article/details/79362094) 。

---

## 模组使能 Secure boot 是否可以再次烧录 ？

- Secure boot 配置为 One-time，那么就只能烧录一次，不可以再重新 烧录 bootloader 固件。
- Secure boot 配置为 Reflashable, 可以重新烧录 bootloader 固件。

---

## 模组使能 flash encrypted, 重新烧录后出现 `flash read error` 错误 ？

> 模组使能 flash encrypted, 重新烧录后，发现会出现 flash read error 的现象.

- 模组使能 flash encrypted 后，模组开启加密功能后将不支持明文固件烧录。
- 可以通过 espefuse.py 脚本将加密关闭后再次烧录，或者已知密钥烧录密文。
- 注意: flash encrypted 加密开关存在次数，仅可重复 3 次。
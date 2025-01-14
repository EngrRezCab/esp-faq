电机控制脉宽调制器 (MCPWM)
================================

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

ESP32 支持使用 MCPWM 的定时器来触发 AD 采样吗？
--------------------------------------------------------------------------------------

  可以在 MCPWM 的定时器事件 ``on_full``、``on_empty``、``on_stop`` 的回调中触发 AD 采样。此外还可以在 MCPWM 的比较器事件 ``on_reach`` 回调中触发 AD 采样。

--------------------

ESP32-S3 能够产生完全互补的 PWM 吗，要求时钟精确，占空比精确，死区可调节？
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  实测 ESP32-S3 可以通过 MCPWM 产生频率 10 k、占空比精度 1 us、死区精度 100 ns 的互补输出波形。

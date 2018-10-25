# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
**are** (Ark Runtime Environment)，机器人运行所依赖的基础库，主要包含运维执行模型定义、
通用执行框架、机器人开发所需的各类基础功能合组件封装。主要模块如下：

* ``loader`` 框架启动模块，该模块会动态加载main模块，并启动Guardian
* ``exception`` 定义了ARK内部的异常类
* ``log`` 日志模块，提供对python标准日志模块的封装，并添加额外功能，具体参考 ``log`` 模块定义
* ``common`` 通用模块，提供了各种常用工具的封装
* ``config`` 配置管理模块
* ``lock`` 该模块基于zookeeper实现了分布式锁功能
* ``client`` 提供了对常用客户端调用的封装，包括请求、结果处理等；并提供了ARK运行必须组件的客户端封装
* ``grapy`` 基于图算法实现的运维执行模式，该模块基于运维场景中常见操作流程，抽象出状态机和工作流两种标准运维作业流程。
* ``state_service`` 状态服务模块，提供状态运行进度展示功能
* ``framework`` 框架核心模块，提供了消息泵机制及感知、决策、执行基类的定义和实现
* ``context`` Guardian运行上下文信息管理模块
* ``sensor`` 感知器模块，提供常见感知模型的实现
* ``decision`` 决策器模块，提供常见决策模型的实现
* ``executor`` 执行器模块，提供常见执行模型的实现
* ``stage`` 包含了分级策略的描述及具体流程
"""
__version = '1.0.0'
__all = ['client', 'common', 'config', 'exception', 'graph',
         'loader', 'lock', 'log', 'server', 'framework', 'context',
         'sensor', 'decision', 'executor', 'stage', ]


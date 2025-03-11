## Android常用的四个分区

*  System分区
   系统分区，存储Android操作系统的核心文件，如framework.jar、系统应用SystemUI.apk等。包含Android框架层（framework）及系统应用（如设置、拨号、短信）。
   默认只读，用户和大多数应用无法修改。需要root权限才能修改。
   在OTA更新时，该分区可能会被替换或修改。
*  Vendor分区
   供应商分区，存储硬件厂商(ORM)提供的驱动程序和HAL(Hardware Abstraction Layer)库，例如：Wi-Fi、蓝牙、相机、传感器等硬件驱动。vendor/lib/目录下的专用库。让Android系统能够适配不同厂商的硬件。该分区通常是SoC厂商(如高通、联发科)预装的内容。
   默认只读，只能在root权限下修改。
System与Vandor的关系：
8.0之前驱动与系统文件混合在/system分区，8.0之后，驱动被移到/vendor，实现系统(AOSP)与硬件驱动的解耦，方便系统升级。
*  Odm分区
*  Product分区
# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AssessQualityRequest(AbstractModel):
    """AssessQuality请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class AssessQualityResponse(AbstractModel):
    """AssessQuality返回参数结构体

    """

    def __init__(self):
        """
        :param LongImage: 取值为TRUE或FALSE，TRUE为长图，FALSE为正常图，长图定义为长宽比大于等于3或小于等于1/3的图片。
        :type LongImage: bool
        :param BlackAndWhite: 取值为TRUE或FALSE，TRUE为黑白图，FALSE为否。黑白图即灰度图，指红绿蓝三个通道都是以灰度色阶显示的图片，并非视觉上的“黑白图片”。
        :type BlackAndWhite: bool
        :param SmallImage: 取值为TRUE或FALSE，TRUE为小图，FALSE为否, 小图定义为最长边小于179像素的图片。当一张图片被判断为小图时，不建议做推荐和展示，其他字段统一输出为0或FALSE。
        :type SmallImage: bool
        :param BigImage: 取值为TRUE或FALSE，TRUE为大图，FALSE为否，定义为最短边大于1000像素的图片
        :type BigImage: bool
        :param PureImage: 取值为TRUE或FALSE，TRUE为纯色图或纯文字图，即没有内容或只有简单内容的图片，FALSE为正常图片。
        :type PureImage: bool
        :param ClarityScore: 综合评分。图像清晰度的得分，对图片的噪声、曝光、模糊、压缩等因素进行综合评估，取值为[0, 100]，值越大，越清晰。一般大于50为较清晰图片，标准可以自行把握。
        :type ClarityScore: int
        :param AestheticScore: 综合评分。图像美观度得分， 从构图、色彩等多个艺术性维度评价图片，取值为[0, 100]，值越大，越美观。一般大于50为较美观图片，标准可以自行把握。
        :type AestheticScore: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LongImage = None
        self.BlackAndWhite = None
        self.SmallImage = None
        self.BigImage = None
        self.PureImage = None
        self.ClarityScore = None
        self.AestheticScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LongImage = params.get("LongImage")
        self.BlackAndWhite = params.get("BlackAndWhite")
        self.SmallImage = params.get("SmallImage")
        self.BigImage = params.get("BigImage")
        self.PureImage = params.get("PureImage")
        self.ClarityScore = params.get("ClarityScore")
        self.AestheticScore = params.get("AestheticScore")
        self.RequestId = params.get("RequestId")


class CarTagItem(AbstractModel):
    """车辆属性识别的结果

    """

    def __init__(self):
        """
        :param Serial: 车系
        :type Serial: str
        :param Brand: 车辆品牌
        :type Brand: str
        :param Type: 车辆类型
        :type Type: str
        :param Color: 车辆颜色
        :type Color: str
        :param Confidence: 置信度，0-100
        :type Confidence: int
        :param Year: 年份，没识别出年份的时候返回0
        :type Year: int
        :param CarLocation: 车辆在图片中的坐标信息
        :type CarLocation: list of Coord
        """
        self.Serial = None
        self.Brand = None
        self.Type = None
        self.Color = None
        self.Confidence = None
        self.Year = None
        self.CarLocation = None


    def _deserialize(self, params):
        self.Serial = params.get("Serial")
        self.Brand = params.get("Brand")
        self.Type = params.get("Type")
        self.Color = params.get("Color")
        self.Confidence = params.get("Confidence")
        self.Year = params.get("Year")
        if params.get("CarLocation") is not None:
            self.CarLocation = []
            for item in params.get("CarLocation"):
                obj = Coord()
                obj._deserialize(item)
                self.CarLocation.append(obj)


class Coord(AbstractModel):
    """汽车坐标信息

    """

    def __init__(self):
        """
        :param X: 横坐标x
        :type X: int
        :param Y: 纵坐标y
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class CropImageRequest(AbstractModel):
    """CropImage请求参数结构体

    """

    def __init__(self):
        """
        :param Width: 需要裁剪区域的宽度，与Height共同组成所需裁剪的图片宽高比例；
输入数字请大于0、小于图片宽度的像素值；
        :type Width: int
        :param Height: 需要裁剪区域的高度，与Width共同组成所需裁剪的图片宽高比例；
输入数字请请大于0、小于图片高度的像素值；
宽高比例（Width : Height）会简化为最简分数，即如果Width输入10、Height输入20，会简化为1：2。
Width : Height建议取值在[1, 2.5]之间，超过这个范围可能会影响效果；
        :type Height: int
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.Width = None
        self.Height = None
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class CropImageResponse(AbstractModel):
    """CropImage返回参数结构体

    """

    def __init__(self):
        """
        :param X: 裁剪区域左上角X坐标值
        :type X: int
        :param Y: 裁剪区域左上角Y坐标值
        :type Y: int
        :param Width: 裁剪区域的宽度，单位为像素
        :type Width: int
        :param Height: 裁剪区域的高度，单位为像素
        :type Height: int
        :param OriginalWidth: 原图宽度，单位为像素
        :type OriginalWidth: int
        :param OriginalHeight: 原图高度，单位为像素
        :type OriginalHeight: int
        :param CropResult: 0：抠图正常；
1：原图过长，指原图的高度是宽度的1.8倍以上；
2：原图过宽，指原图的宽度是高度的1.8倍以上；
3：抠图区域过长，指抠图的高度是主体备选框高度的1.6倍以上；
4：抠图区域过宽，指当没有检测到人脸时，抠图区域宽度是检测出的原图主体区域宽度的1.6倍以上；
5：纯色图，指裁剪区域视觉较为单一、缺乏主体部分 ；
6：宽高比异常，指Width : Height取值超出[1, 2.5]的范围；

以上是辅助决策的参考建议，可以根据业务需求选择采纳或忽视。
        :type CropResult: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.OriginalWidth = None
        self.OriginalHeight = None
        self.CropResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.OriginalWidth = params.get("OriginalWidth")
        self.OriginalHeight = params.get("OriginalHeight")
        self.CropResult = params.get("CropResult")
        self.RequestId = params.get("RequestId")


class DetectCelebrityRequest(AbstractModel):
    """DetectCelebrity请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectCelebrityResponse(AbstractModel):
    """DetectCelebrity返回参数结构体

    """

    def __init__(self):
        """
        :param Faces: 公众人物识别结果数组。如果检测不到人脸，返回为空；最多可以返回10个人脸识别结果。
        :type Faces: list of Face
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Faces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Faces") is not None:
            self.Faces = []
            for item in params.get("Faces"):
                obj = Face()
                obj._deserialize(item)
                self.Faces.append(obj)
        self.RequestId = params.get("RequestId")


class DetectDisgustRequest(AbstractModel):
    """DetectDisgust请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectDisgustResponse(AbstractModel):
    """DetectDisgust返回参数结构体

    """

    def __init__(self):
        """
        :param Confidence: 对于图片中包含恶心内容的置信度，取值[0,1]，一般超过0.5则表明可能是恶心图片。
        :type Confidence: float
        :param Type: 与图像内容最相似的恶心内容的类别，包含腐烂、密集、畸形、血腥、蛇、虫子、牙齿等。
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectLabelItem(AbstractModel):
    """图像标签检测结果。

    """

    def __init__(self):
        """
        :param Name: 图片中的物体名称。
        :type Name: str
        :param Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定。
        :type Confidence: int
        :param FirstCategory: 标签的一级分类
        :type FirstCategory: str
        :param SecondCategory: 标签的二级分类
        :type SecondCategory: str
        """
        self.Name = None
        self.Confidence = None
        self.FirstCategory = None
        self.SecondCategory = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")
        self.FirstCategory = params.get("FirstCategory")
        self.SecondCategory = params.get("SecondCategory")


class DetectLabelRequest(AbstractModel):
    """DetectLabel请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        :param Scenes: 本次调用支持的识别场景，可选值如下：
WEB，针对网络图片优化;
CAMERA，针对手机摄像头拍摄图片优化;
ALBUM，针对手机相册、网盘产品优化;
如果不传此参数，则默认为WEB。

支持多场景（Scenes）一起检测。例如，使用 Scenes=["WEB", "CAMERA"]，即对一张图片使用两个模型同时检测，输出两套识别结果。
        :type Scenes: list of str
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.Scenes = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.Scenes = params.get("Scenes")


class DetectLabelResponse(AbstractModel):
    """DetectLabel返回参数结构体

    """

    def __init__(self):
        """
        :param Labels: Web网络版标签结果数组。如未选择WEB场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param CameraLabels: Camera摄像头版标签结果数组。如未选择CAMERA场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param AlbumLabels: Album相册版标签结果数组。如未选择ALBUM场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Labels = None
        self.CameraLabels = None
        self.AlbumLabels = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self.CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self.AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.AlbumLabels.append(obj)
        self.RequestId = params.get("RequestId")


class DetectMisbehaviorRequest(AbstractModel):
    """DetectMisbehavior请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectMisbehaviorResponse(AbstractModel):
    """DetectMisbehavior返回参数结构体

    """

    def __init__(self):
        """
        :param Confidence: 对于图片中包含不良行为的置信度，取值[0,1]，一般超过0.5则表明可能包含不良行为内容；
        :type Confidence: float
        :param Type: 图像中最可能包含的不良行为类别，包括赌博、打架斗殴、吸毒等。
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectProductRequest(AbstractModel):
    """DetectProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectProductResponse(AbstractModel):
    """DetectProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Products: 商品识别结果数组
        :type Products: list of Product
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class EnhanceImageRequest(AbstractModel):
    """EnhanceImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class EnhanceImageResponse(AbstractModel):
    """EnhanceImage返回参数结构体

    """

    def __init__(self):
        """
        :param EnhancedImage: 增强后图片的base64编码。
        :type EnhancedImage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnhancedImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnhancedImage = params.get("EnhancedImage")
        self.RequestId = params.get("RequestId")


class Face(AbstractModel):
    """公众人物识别人脸信息

    """

    def __init__(self):
        """
        :param Name: 与图片中人脸最相似的公众人物的名字。
        :type Name: str
        :param Labels: 公众人物身份标签的数组，一个公众人物可能有多个身份标签。
        :type Labels: list of Labels
        :param BasicInfo: 对人物的简介。
        :type BasicInfo: str
        :param Confidence: 算法对于Name的置信度（图像中人脸与公众人物的相似度），0-100之间，值越高，表示对于Name越确定。
当Confidence低于70分时，Name仅供参考。您可以根据业务实际情况调整阈值。
        :type Confidence: int
        :param X: 人脸区域左上角横坐标。
        :type X: int
        :param Y: 人脸区域左上角纵坐标。
        :type Y: int
        :param Width: 人脸区域宽度。
        :type Width: int
        :param Height: 人脸区域高度。
        :type Height: int
        :param ID: 公众人物的唯一编号，可以用于区分同名人物、一个人物不同称呼等情况。唯一编号为8个字符构成的字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self.Name = None
        self.Labels = None
        self.BasicInfo = None
        self.Confidence = None
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.ID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Labels()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.BasicInfo = params.get("BasicInfo")
        self.Confidence = params.get("Confidence")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ID = params.get("ID")


class Labels(AbstractModel):
    """名人识别的标签

    """

    def __init__(self):
        """
        :param FirstLabel: 公众人物身份标签的一级分类，例如体育明星、娱乐明星、政治人物等；
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstLabel: str
        :param SecondLabel: 公众人物身份标签的二级分类，例如歌手（对应一级标签为“娱乐明星”）；
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondLabel: str
        """
        self.FirstLabel = None
        self.SecondLabel = None


    def _deserialize(self, params):
        self.FirstLabel = params.get("FirstLabel")
        self.SecondLabel = params.get("SecondLabel")


class Product(AbstractModel):
    """检测到的单个商品结构体

    """

    def __init__(self):
        """
        :param Name: 图片中商品的三级分类识别结果，选取所有三级分类中的置信度最大者
        :type Name: str
        :param Parents: 三级商品分类对应的一级分类和二级分类，两级之间用“-”（中划线）隔开，例如商品名称是“硬盘”，那么Parents输出为“电脑、办公-电脑配件”
        :type Parents: str
        :param Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定
        :type Confidence: int
        :param XMin: 商品坐标X轴的最小值
        :type XMin: int
        :param YMin: 商品坐标Y轴的最小值
        :type YMin: int
        :param XMax: 商品坐标X轴的最大值
        :type XMax: int
        :param YMax: 商品坐标Y轴的最大值
        :type YMax: int
        """
        self.Name = None
        self.Parents = None
        self.Confidence = None
        self.XMin = None
        self.YMin = None
        self.XMax = None
        self.YMax = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Parents = params.get("Parents")
        self.Confidence = params.get("Confidence")
        self.XMin = params.get("XMin")
        self.YMin = params.get("YMin")
        self.XMax = params.get("XMax")
        self.YMax = params.get("YMax")


class RecognizeCarRequest(AbstractModel):
    """RecognizeCar请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class RecognizeCarResponse(AbstractModel):
    """RecognizeCar返回参数结构体

    """

    def __init__(self):
        """
        :param CarCoords: 汽车的四个矩形顶点坐标，如果图片中存在多辆车，则输出最大车辆的坐标。
        :type CarCoords: list of Coord
        :param CarTags: 车辆属性识别的结果数组，如果识别到多辆车，则会输出每辆车的top1结果。
        :type CarTags: list of CarTagItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CarCoords = None
        self.CarTags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self.CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self.CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self.CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self.CarTags.append(obj)
        self.RequestId = params.get("RequestId")
# tfjs_try
TFJSでワンページのHTMLを作るトライ
TFJSのモデル
・画像分類：mobilenet, mobilenetV2
・物体検出：coco-ssd, tfjs-yolo-tiny
・セマンティックセグメンテーション：deeplab
・音声検出：speech-commands


#1 CDNで使用する方法(CDNを使うので外部とのネットワーク接続に依存する)
HTMLへのscript表記で下記を使うことで使用できる
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs/dist/tf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@1.0.0"></script>


#2 CDNを使わずにサーバのローカルにおいて使用する場合
npmを使ってtensorflowjsとtensorflow-modelsをインストールする
npm install @tensorflow/tfjs
npm install @tensorflow-models/mobilenet

HTMLで下記の様にscriptを表記する事で使用できる
<!--<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs/dist/tf.min.js"></script>-->
<script src="./static/js/@tensorflow/tfjs/dist/tf.min.js"></script>
<!--<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet@1.0.0"></script>-->
<script src="./static/model/@tensorflow-models/mobilenet/dist/mobilenet.min.js"></script>
  
#3 自作のカスタムモデルを使いたい場合
カスタムモデルを使用したい場合は、PythonのTensorflowでモデル作成し、Pythonライブラリのtensorflowjsを使ってコンバートする事で、
model.jsonと重みファイル(.bin)を取得して使うことができる


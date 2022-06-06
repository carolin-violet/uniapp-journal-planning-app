<template>
	<view class="article-layout">
		<view class="article-body">
			<view class="article-head">
				<!-- 标题 -->
				<view class="title">
					{{article.title}}
				</view>
				
				<!-- 作者 -->
				<view class="author">
					{{article.author}}
				</view>
			</view>
			
				
				<!-- 正文内容 -->
				<view class="article-content">
					<text class="paragraph" v-for="(item, index) in article.content">
						{{item}}
					</text>
					<view class="icons">
						<text class="iconfont" :class="isCollected ? 'icon-shoucang1': 'icon-shoucang'" @click="handleCollect"></text>
						<text class="iconfont icon-shoucangjia" @click="toCollect"></text>
					</view>
				</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				article: {},
				isCollected: false,
				article_id: 0
			}
		},
		onLoad() {
			this.getArticle()
		},
		methods: {
			async getArticle() {
				this.article = {}
				this.isCollected = false
				let res = await this.myRequest({
					url: "/articles/random"
				})
				this.article = res.data
				uni.stopPullDownRefresh()
			},
			async handleCollect() {
				this.isCollected = !this.isCollected
				if (this.isCollected === true) {
					let res = await this.myRequest({
						url: "/articles",
						method: "POST",
						data: this.article,
					})
					this.article_id = res.data.article_id
				} else {
					let res = await this.myRequest({
						url: "/articles/" + this.article_id,
						method: "DELETE"
					})
					console.log(res)
				}
			},
			toCollect() {
				uni.navigateTo({
					url: "../collected/collected"
				})
			}
		},
		onPullDownRefresh() {
			this.getArticle()
			setTimeout(() => {
				uni.stopPullDownRefresh()
			}, 1500)
		}
	}
</script>

<style lang="less" scoped>
	.article-layout{
		height: 100%;
		background: url(../../static/wallpapers/d5676dbfe101b43f0f8ad5757766cd98.webp) no-repeat fixed;
		background-size: 100%;
		padding: 20rpx 20rpx;
		.article-body{
			height: 1400rpx;
			overflow: auto;
			background-color: rgba(200, 200, 200, 0.6);
			.article-head{
				margin-top: 30rpx;
				text-align: center;
				.title{
					font-size: 60rpx;
					height: 160rpx;
					line-height: 80rpx;
					word-wrap: break-word;
				}
				.author{
					font-size: 30rpx;
					height: 60rpx;
					line-height: 60rpx;
				}
			}
			.article-content{
				display: flex;
				flex-direction: column;
				padding: 30rpx 20rpx;
				.paragraph{
					font-size: 30rpx;
					text-indent: 60rpx;
				}
				.icons{
					display: flex;
					flex-direction: row-reverse;
					height: 100rpx;
					width: 100%;
					line-height: 100rpx;
					.iconfont{
						font-size: 70rpx;
						text-align: center;
						margin: 10rpx;
					}
					.icon-shoucangjia{
						color: #7FFF00;
					}
					.icon-shoucang{
						color: #FFFFFF;
					}
					.icon-shoucang1{
						color: #f00;
					}
				}
			}
		}
	}
</style>

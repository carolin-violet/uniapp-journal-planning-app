<template>
	<view class="collected-layout">
		<view class="contents-layout">
			<view class="collected-item" v-for="(item, index) in collects" :key="item.article_id">
				<view class="left">
					<image :src="'../../static/ACG-collected/' + imgList[index% imgList.length]" mode=""></image>
				</view>
				<view class="right">
					<text class="content" @click="toArticleDetail(item.article_id)">{{item.title}}——{{item.author}}</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imgList: ['2kpkkx.webp', '83yre2.webp', 'dgwx7j.webp', 'g8oyp7.webp', 'j5w775.webp', 'j5x265.webp', 'j5xpom.webp', 'j8d29q.webp', 'j8l9lm.webp', 'j8rv8w.webp'],
				collects: []
			}
		},
		methods: {
			async getCollects() {
				let res = await this.myRequest({
					url: "/articles"
				})
				this.collects = res.data.articles
			},
			toArticleDetail(article_id) {
				uni.navigateTo({
					url: "../articleDetail/articleDetail?article_id=" + article_id
				})
			}
		},
		onLoad() {
			this.getCollects()
		},
		onPullDownRefresh() {
			this.getCollects()
			setTimeout(()=> {
				uni.stopPullDownRefresh()
			}, 1500)
		}
	}
</script>

<style lang="less" scoped>
	.collected-layout{
		height: 100%;
		width: 100%;
		background: url(../../static/wallpapers/ce3d8834d946786c122cd94ca969fbb0.webp) no-repeat fixed;
		background-size: 100%;
		.contents-layout{
			height: 1400rpx;
			overflow: auto;
			width: 100%;
			background-color: rgba(200,200,200,0.7);
			.collected-item{
				box-shadow: 0 0 15px rgb(50,50,50);
				background-color: rgba(100,100,100, 0.4);
				border-radius: 20rpx;
				margin: 60rpx auto;
				width: 80%;
				height: 250rpx;
				display: flex;
				justify-content: center;
				box-sizing: border-box;
				.left{
					width: 400rpx;
					height: 250rpx;
					image{
						width: 100%;
						height: 100%;
					}
				}
				.right{
					display: inline-block;
					width: 200rpx;
					height: 250rpx;
					margin-top: 50rpx;
					.content{
						font-size: 25rpx;
						line-height: 30rpx;
						letter-spacing: 5rpx;
						padding: 0 20rpx;
						overflow: hidden;
					}
				}
			}
		}
	}
</style>

<template>
	<view class="navContent">
		<view v-for="item in navContents['content']" :key="item.id" @click="toNewUrl(item.url)" class="content-item">
			<image :src="item.img_url ? item.img_url : '../../static/9866091_carolin-zhou_1634606834.png'" mode=""></image>
			<view>
				<text>{{item.title}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"navContent",
		props: ['navContents'],
		data() {
			return {
				
			};
		},
		methods: {
			toNewUrl(url) {
				uni.navigateTo({
					url: "../../pages/navUrl/navUrl?url=" + url
				})
			}
		}
	}
</script>

<style lang="less" scoped>
	.navContent{
		width: 100%;
		height: 1400rpx;
		display: flex;
		flex-wrap: wrap;
		overflow: auto;
		background-color: rgba(100,100,100, 0.8);
		.content-item{
			width: 150rpx;
			height: 220rpx;
			margin: 10rpx 40rpx;
			image{
				width: 150rpx;
				height: 150rpx;
			}
			view{
				text-align: center;
			}
		}
	}
</style>

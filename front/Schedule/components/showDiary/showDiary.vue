<template>
	<view class="diaries-show">
		<view class="diary-item" v-for="item in diaries" :key="item.id">
			<view class="item-image">
				<image :src="imgPath+imgList[item.id%imgList.length]" mode="scaleToFill"></image>
			</view>
			<view class="item-date">
				<text @click="toDiaryDetail(item.id)">{{item.date}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	import {dateFormat} from "../../utils/dateFormat.js"
	export default {
		name:"showDiary",
		props: ['toRefresh'],
		data() {
			return {
				diaries: [],
				imgPath: "../../static/ACG-diaryicon/",
				imgList: ['[2242]64711786.jpg', '[2268]66016094.png', '[2324]65932398.png', '[30807]60141148.png', '[35396]60268880.jpg', '[43809]62608184.png', '[45055]60107386.png', '[50033]Hotaru-64495434.png', '[73618]Autumn-60095408.jpg', '[79748]59665299.png', '[84173]glow-33703665.png']
			}
		},
		methods: {
			async getDiaries() {
				let res = await this.myRequest({
					url: "/diaries"
				})
				this.diaries = res.data.diaries
			},
			toDiaryDetail(diary_id) {
				uni.navigateTo({
					url: "../../pages/diaryDetail/diaryDetail?diary_id=" + diary_id
				})
			}
		},
		created() {
			this.getDiaries()
		},
		mounted() {
			setInterval(() => {
				if (this.toRefresh === 1) {
					this.getDiaries()
				}
			}, 3000)
		}
	}
</script>

<style lang="less" scoped>
	.diaries-show{
		height: 100%;
		overflow: auto;
		display: flex;
		flex-direction: column;
		.diary-item{
			margin: 30rpx auto;
			width: 600rpx;
			height: 250rpx;
			border-radius: 10rpx;
			box-shadow: 0 0 15rpx rgb(42, 223, 144);
			text-shadow: 0 0 15rpx rgba(82, 228, 238,1);
			display: flex;
			.item-image{
				width: 350rpx;
				height: 100%;
				image{
					width: 100%;
					height: 100%;
				}
			}
			.item-date{
				width: 250rpx;
				height: 100%;
				text{
					display: inline-block;
					margin: 50rpx 15rpx;
					letter-spacing: 10rpx;
				}
			}
		}
	}

</style>

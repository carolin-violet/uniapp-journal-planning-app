<template>
	<view>
		<textarea placeholder-style="color: rgba(42, 223, 144, 0.7)" class="writing-diary" placeholder="请在此区域写日记" maxlength="500" v-model="diary"/>
		<button @click="submitDiary" type="primary">提交</button>
	</view>
</template>

<script>
	import {dateFormat} from "../../utils/dateFormat.js"
	export default {
		name:"writeDiary",
		data() {
			return {
				diary: '',
			};
		},
		methods:{
			async submitDiary() {
				let date =  dateFormat("YYYY-mm-dd HH:MM:SS", new Date())
				let data = {
					date,
					content: this.diary
				}
				let res = await this.myRequest({
					url: "/diaries",
					method: "POST",
					data
				})
				if (res.data.msg === "上传成功") {
					this.diary = '',
					uni.showToast({
						title: "上传成功"
					})
				}
			}
		}
	}
</script>

<style lang="less" scoped>
	.writing-diary{
		width: 700rpx;
		height: 1000rpx;
		border-radius: 10rpx;
		box-shadow: 0 0 15rpx rgb(42, 223, 144);
		margin: 10rpx auto;
		overflow: auto;
		background-color: rgba(255,255,255,0.3);
		color: rgb(42, 223, 144);
	}
	button{
		margin: 20rpx auto;
		background-image: linear-gradient(to right, rgba(76,236,244,0.7), rgba(216,140,237,0.7));
		opacity: 0.7;
		width: 400rpx;
	}
</style>

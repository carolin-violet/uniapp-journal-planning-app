<template>
	<view class="plan-layout" :style="{backgroundImage: 'url('+imgUrl+')'}">
		<view class="todo-layout">
			<!-- 上半部分 -->
			<view class="make-plan">
				<view class="choose-datetime">
					<button  @click="onShowDatePicker('datetime')">选择开始时间</button>
					<button  @click="onShowDatePicker('datetime2')">选择截止时间</button>
				</view>
				<view class="time"  v-if="datetime && datetime2">
					{{datetime}} 至 {{datetime2}}
				</view>
				<textarea placeholder-style="color:#fff" type="text" placeholder="请在选择时间段后写入计划并提交" maxlength="50" adjust-position v-model="plan"></textarea>
				<button @click="submitPlan">提交计划</button>
			</view>
			
			<!-- 下半部分 -->
			<view class="query-plan" v-if="todayPlans.length">
				<view class="des">
					<text>时间段</text>
					<text>内容</text>
					<text>已完成</text>
				</view>
				<!-- 今日计划主体内容 -->
				<view class="plans-today">
					<view class="plan-item" v-for="item in todayPlans" :key="item.id">
						<text>{{item.startTime}}--{{item.endTime}}</text>
						<text>{{item.content}}</text>
						<text class="iconfont icon-xuanzhongxuanzhong" :class="item.completed == 1 ? 'completed': '' " @click="changeCompleted(item.id)"></text>
					</view>
				</view>
				<!-- 小功能 -->
				<view class="submitCompleted">
					<button @click="updatePlans">确认已完成的情况</button>
				</view>
			</view>
			<!-- 任务都完成后的界面 -->
			<view class="completed-tip" v-else>
				今日任务全部完成咯
				<text class="iconfont icon-xiaolian1"></text>
			</view>

		</view>
		<mx-date-picker :show="showPicker" :type="type" :value="value" :show-tips="true" :begin-text="'入住'" :end-text="'离店'" :show-seconds="true" @confirm="onSelected" @cancel="onSelected" />
	</view>
</template>
<script>
	import MxDatePicker from "@/components/mx-datepicker/mx-datepicker.vue"
	import {dateFormat} from "../../utils/dateFormat.js"
	
	export default {
		components: {
			MxDatePicker,
		},
		data() {
			return {
				showPicker: false,
				date: '2021/01/01',
				time: '15:00:12',
				datetime: '',  // 开始时间
				datetime2: '',  // 截止时间
				plan: '',  // 计划内容
				range: ['2021/01/01','2022/01/06'],
				rangetime: ['2021/01/08 14:00','2022/01/16 13:59'],
				type: 'rangetime',
				value: '',
				today: "",  // 当天的日期
				todayPlans: []  ,// 当天的计划
				imgPath: '../../static/ACG-plans/',
				imgUrl: '',
				imgList: ['05c50886e7414021b992f8881f0d37a1.webp', '06015ac5f395470c849314dfae02a829.webp', '0a50e914cfbf46f98f9f1aab071ca19c.webp', '0ad6221525e0496daf3735c007968113.webp', '0c609ca0c50840e1b5637c9a374833e1.webp', '0e9fd8359916418d9466cbf7a3265744.webp', '140068f6c9354bb0bde9eabfa3d1f7f0.webp', '183ff4f8c2154e8b8642983f2da7c564.webp', '196bc9c3bf834c7f8017c57539ef254c.webp', '1abd0a89c13e45a38f9d847562f638b5.webp', '1c566df0fda94a2d8990ea5e8bcecf65.webp', '1d855fcdb6004017a55a0ff7ba8bea43.webp', '228b7bd66b1a432aad676d69b9e15f02.webp', '26f20efd2fb74c118a96c5129f18323a.webp', '2fa8288d850f4556b7171e4d15122d91.webp', '367d34a006d747f3b786f5f4b1d22371.webp', '375b187b294c4c0695203d9b81ac040e.webp', '38044eb12ae44ebd8c26013024ec6897.webp', '38916565c486452db09e14f3ffcdd39a.webp', '396c3e77c6de4f3c84978416fa197f46.webp', '3a3787a8a971452c9cdf1a296a412854.webp', '3b3589a34c254b65ac8b248303ced4df.webp', '40c1b2594b4544b4a7916bd0f087652e.webp', '41ab29be8a964ef49db35ea8cc464155.webp', '44e377e3efb147799ea02ff2f22cbd78.webp', '4858af4ffc4344169e2d716cf9caca7a.webp', '4906faab95954dadb35350d8dd53c924.webp', '4cc2e5d6ac7c4beea80b9397d8e25655.webp', '4f6ef5a2220648b9956c2813ef46e9ca.webp', '50c1d95f26c944f7bf52fc0898f01ce7.webp', '553fb2527da8485b8bdb0492b2283ef9.webp', '5d7e99fa7d3840c5a07bb07a83655baa.webp', '5f3cf1cc85d748c18835d807ea9ef2d7.webp', '613d22b16a614c158572473bb7ee4ebf.webp', '63393b823cac48f694a729b8d496c305.webp', '65b36ab5e6ef4cb4bdd2c5028ab3c406.webp', '697a4e43c38c4f688b702ff7f37aac13.webp', '727cd1e618cd4a46a49962fbcfa95969.webp', '7c3ab843522049e180db5ad33098913f.webp', '7e6e3a7b53724d0883e96be7381dcae3.webp', '81457e991e3d430ea14dd050820cdc9c.webp', '81e74d96a1704bfbba7a0a7ad084a30d.webp', '83ea1d6454de439fa7bbe8df2b1a58b9.webp', '87832ca676f141a280d0659e234ae80b.webp', '899cf0b507494c5083b84f762c9fef9d.webp', '8e855e52077244e9b696659a0b6720cb.webp', '9303a50c53b1474db2cb7d5f92ae81d4.webp', '9310abf556474890872622b6e3d2b010.webp', '93297bc78eee4aa292ea66d7e71fbfab.webp', '95d91c12da114ae699eb845dbb11dbe0.webp', '9999bb8f5bee4580a1be7c3ca9af07a0.webp', '9c4c400f8ee549cf8c3d2463a7a7ad0f.webp', '9cad8b17f04247e18b8615396d569799.webp', 'a0334e43e22b4e3aaedc2786d22e44c0.webp', 'a1fc5faf960f4d6680cd635f72c9f834.webp', 'a4957e59ecd44f73aefedd730aba90a0.webp', 'a5495334c2b84b07b874e76827ff0999.webp', 'a67bc78956024b85934b29ab75dc78f3.webp', 'a8f7e07e3e1341858c34a1aebec7f90a.webp', 'a9d73a2d0b6c44bd8ee16c25a3d94f5b.webp', 'aa80b05126184c30bcb73376f31788e4.webp', 'afa6bbf0e02f45bab86453092f94f7fd.webp', 'b17ccf66cf264c5799bf30fa60963ee2.webp', 'b17dd1c054ef40f7aec2cc3bfa5ab18f.webp', 'b1bfc0ec4ee24b6982faf54729ee71b9.webp', 'b21d692875974d8eb05184a126b62dcf.webp', 'b2316b23b0994be4a65a975d74824283.webp', 'ba1e2692e4324928b4a2ddc930f64b59.webp', 'bc3d652cef424742bdc809af41e04ed4.webp', 'bd394b47665b4044bff279c82477a414.webp', 'c003bcf76d014dbfb160e0c0a1aafcaf.webp', 'c130abd6a5104fcfa834004cae3ccbca.webp', 'c225f2d4b4a9428c8dfda72fcb78091e.webp', 'c719bf728d12463f83f2f6d9b1ba2d69.webp', 'c76e0877acfb4e24acf353b5fb427058.webp', 'cc9ff9e9b4c24c559fe6e775ceaffdf6.webp', 'd1151dcd4bfd4785b92f80402bab3925.webp', 'd4fde10ec1fd4975b2beb00ae2cbeeb0.webp', 'd5f8feabfcad4cc9af97ca6f2136f01c.webp', 'de1013d878c744cb927b36c70059314d.webp', 'de1ba06d399244f0ba833690231aab37.webp', 'e0a22dfa1b9948dc9145cc60e6386f37.webp', 'edca7f0d204248389ff554e0c10aa7bb.webp', 'ee2c2103bf4a490c9ee4ca66cd6cb665.webp', 'f0764b52bd3d463bbbf6bd95d382e7cc.webp', 'f0ceb49a7b314113b17732a741aca9cf.webp', 'f20e8d46d86447a4b41ba763b1a6b67f.webp', 'f971b588d50845c78aad1385d5f64bbc.webp', 'fcf58c4992024438b0857dac82195188.webp', 'rBAAdmF4tDOAf2omAAJiwOxGbgw670.webp', 'rBAAdmF4tH-AbWUdAAHMu39jnSk548.webp', 'rBAAdmF4tH2AeCFKAAF3Nkv1tWc733.webp', 'rBAAdmF4tHeABd_OAAGZ87V6pXI763.webp', 'rBAAdmF4tIeAYDV-AAJDdNWS8nc783.webp', 'rBAAdmF4tIKAITCUAAF2srVO34w659.webp', 'rBAAdmF4tIOABuChAAHt5FdY3JI485.webp', 'rBAAdmF4tISARW9TAAFUBJ4AmO0084.webp', 'rBAAdmF4tj6ASf70AAHcLyhFXSg650.webp', 'rBAAdmF4tjqAKHIRAAG0AHRE1uE891.webp', 'rBAAdmF4tjyAJCd1AAHGD1WNy00192.webp', 'rBAAdmF4tkSAaXEFAAH8bBuQhXw848.webp', 'rBAAdmF4tyqAUnPdAAGKrDG6A8Y155.webp']
			}
		},
		methods: {
			onShowDatePicker(type){//显示
				this.type = type;
				this.showPicker = true;
				this.value = this[type];
			},
			onSelected(e) {//选择
				this.showPicker = false;
				if(e) {
					this[this.type] = e.value; 
					//选择的值
					console.log('value => '+ e.value);
					//原始的Date对象
					console.log('date => ' + e.date);
				}
			},
			async submitPlan() {
				let data = {
					startTime: this.datetime,
					endTime: this.datetime2,
					content: this.plan,
					completed: 0
				}
				let res = await this.myRequest({
					url: "/plans",
					data,
					method: 'POST',
				})
				this.plan = ''
				uni.startPullDownRefresh()
			},
			async getPlans() {
				let res = await this.myRequest({
					url: "/plans",
					data: {
						date: this.today
					}
				})
				this.todayPlans = res.data.plans
			},
			changeCompleted(id) {
				let newtodayPlans = this.todayPlans.map((item) =>{
					if (item.id === id){
						if (item.completed == 1) item.completed = 0
						else item.completed = 1
					}
					return item
				})
				this.todayPlans = newtodayPlans
			},
			async updatePlans() {
				let completedPlans = this.todayPlans.map(item => {
					if (item.completed === 1) return {
						id: item.id,
						completed: item.completed
					}
				})
				let data = {
					data: completedPlans,
					msg: "update"
				}
				let res = await this.myRequest({
					url: "/plans/update",
					method: "POST",
					data: data
				})
				uni.startPullDownRefresh()
			}
		},
		onLoad() {
			this.imgUrl = this.imgPath+this.imgList[Math.floor(Math.random()*this.imgList.length)]
			let date = new Date()
			this.today =  dateFormat("YYYY-mm-dd", date)
			this.datetime = dateFormat("YYYY-mm-dd HH:MM:SS", date)
			this.datetime2 = this.today + " 23:59:59"
			this.getPlans()
		},
		onPullDownRefresh() {
			this.getPlans()
			setTimeout(() => {
				uni.stopPullDownRefresh()
			}, 1500)
    }
	}
</script>
<style lang="less" scoped>
	.plan-layout{
		width: 100%;
		height: 100%;
		background-size: cover;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-position: center center;
		color: #fff;
		button{
			background-image: linear-gradient(to right, rgba(76,236,244,0.7), rgba(216,140,237,0.7));
			opacity: 0.5;
		}
		.todo-layout{
			width: 100%;
			height: 1200rpx;
			overflow: auto;
			background-color: rgba(50,50,50,0.5);
			.make-plan{
				margin-top: 100rpx;
				.choose-datetime{
					display: flex;
					button{
						width: 300rpx;
						height: 100rpx;
					}
				}
				.time{
					text-align: center;
					height: 60rpx;
					line-height: 60rpx;
					font-size: 30rpx;
				}
				textarea{
					width: 700rpx;
					margin: 0 auto;
					border: 1px solid rgb(200,200,200);
					border-radius: 10rpx;
					height: 140rpx;
					line-height: 60rpx;
				}
				button{
					width: 400rpx;
					height: 100rpx;
					margin: 10rpx auto;
				}
			}
			.query-plan{
				margin: 20rpx 0;
				text-align: center;
				.des{
					display: flex;
					height: 60rpx;
					text{
						flex: 1;
					}
				}
				.plans-today{
					height: 500rpx;
					overflow: auto;
					.plan-item{
						display: flex;
						height: 120rpx;
						line-height: 40rpx;
						box-sizing: border-box;
						text{
							font-size: 20rpx;
							flex: 1;
							word-wrap: break-word;
						}
						.iconfont{
							font-size: 50rpx;
							color: rgb(150,150,150);
						}
						.completed{
							color: rgb(140, 237, 167);
						}
					}
				}
				.submitCompleted{
					margin: 30rpx 0;
					button{
						width: 350rpx;
					}
				}
			}
			.completed-tip{
				margin: 100rpx 0;
				text-align: center;
				color: rgba(76,236,244,0.7);
				font-size: 60rpx;
				.iconfont{
					font-size: 60rpx;
				}
			}
		}
	}
</style>
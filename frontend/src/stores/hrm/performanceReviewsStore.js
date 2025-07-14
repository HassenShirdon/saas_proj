import { defineStore } from 'pinia'
import * as performanceApi from '@/api/hrm'
export const usePerformanceReviewsStore = defineStore('performanceReviews', {
  state: () => ({
    reviews: [],
    loading: false,
  }),
  actions: {
    async fetchReviews() {
      this.loading = true
      const res = await performanceApi.getPerformanceReviews()
      this.reviews = res.data
      this.loading = false
    },
    async addReview(review) {
      await performanceApi.createPerformanceReview(review)
      await this.fetchReviews()
    },
    async updateReview(id, review) {
      await performanceApi.updatePerformanceReview(id, review)
      await this.fetchReviews()
    },
    async removeReview(id) {
      await performanceApi.deletePerformanceReview(id)
      await this.fetchReviews()
    },
  },
})

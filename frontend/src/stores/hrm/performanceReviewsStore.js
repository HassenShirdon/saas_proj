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
      const res = await performanceApi.getReviews()
      this.reviews = res.data
      this.loading = false
    },
    async addReview(review) {
      await performanceApi.createReview(review)
      await this.fetchReviews()
    },
    async updateReview(id, review) {
      await performanceApi.updateReview(id, review)
      await this.fetchReviews()
    },
    async removeReview(id) {
      await performanceApi.deleteReview(id)
      await this.fetchReviews()
    },
  },
})

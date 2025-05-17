<template>
  <div>
    <HeroSection />
    <FeaturesSection />
    <PricingSection />
    <TestimonialSection />
    <CtaSection />
    <FooterSection />
  </div>
</template>

<script>
import HeroSection from '@/components/landing/HeroSection.vue'
import FeaturesSection from '@/components/landing/FeatureSection.vue'
import PricingSection from '@/components/landing/PricingSection.vue'
import TestimonialSection from '@/components/landing/TestimonialsSection.vue'
import CtaSection from '@/components/landing/CallToAction.vue'
import FooterSection from '@/components/landing/FooterSection.vue'

export default {
  name: 'LandingPage',
  components: {
    HeroSection,
    FeaturesSection,
    PricingSection,
    TestimonialSection,
    CtaSection,
    FooterSection,
  },
}
</script>

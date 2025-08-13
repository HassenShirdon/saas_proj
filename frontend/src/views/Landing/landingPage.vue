<template>
  <div class="container-fluid" style="background: #f0f0f0;">
    <navigationSection />
    <HeroSection />
    <FeaturesSection />
    <Aboutsection />
    <PricingSection />
    <TestimonialSection />
    <CtaSection />
    <FooterSection />
  </div>
</template>

<script>
import navigationSection from '@/components/landing/navigationSection.vue'
import HeroSection from '@/components/landing/HeroSection.vue'
import FeaturesSection from '@/components/landing/FeatureSection.vue'
import PricingSection from '@/components/landing/PricingSection.vue'
import TestimonialSection from '@/components/landing/TestimonialsSection.vue'
import CtaSection from '@/components/landing/CallToAction.vue'
import FooterSection from '@/components/landing/FooterSection.vue'
import Aboutsection from '@/components/landing/Aboutus.vue'

export default {
  name: 'LandingPage',
  components: {
    navigationSection,
    HeroSection,
    Aboutsection,
    FeaturesSection,
    PricingSection,
    TestimonialSection,
    CtaSection,
    FooterSection,
  },
}
</script>

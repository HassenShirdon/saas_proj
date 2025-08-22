<template>
  <LandingLayout>
    <Header />
    <Hero />
    <Features />
    <About />
    <Pricing />
    <CallToAction />
    <Footer />
  </LandingLayout>
</template>

<script setup>
import LandingLayout from '../layouts/LandingLayout.vue'
import Header from '../components/landing/Header.vue'
import Hero from '../components/landing/Hero.vue'
import Features from '../components/landing/Features.vue'
import About from '../components/landing/About.vue'
import Pricing from '../components/landing/Pricing.vue'
import CallToAction from '../components/landing/CallToAction.vue'
import Footer from '../components/landing/Footer.vue'
</script>

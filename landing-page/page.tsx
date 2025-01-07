import { Github } from 'lucide-react'
import Link from 'next/link'

export default function LandingPage() {
  // Placeholder for your personal GitHub URL
  const personalGithubUrl = "https://github.com/ishacm/nia-ai-assistant.git"

  return (
    <div className="min-h-screen bg-background text-text font-sans">
      <main className="container mx-auto px-4 py-8 md:py-16">
        <header className="text-center mb-12 md:mb-16">
          <h1 className="text-4xl md:text-6xl font-bold mb-4 text-accent">NIA - Neural Intelligent Aide</h1>
          <p className="text-xl md:text-2xl text-text/80">Your personal AI powered assistant.</p>
        </header>

        <section className="mb-12 md:mb-16 bg-gray-900 text-white p-8 rounded-lg">
          <h2 className="text-3xl md:text-4xl font-semibold mb-8 text-orange-500 border-b-2 border-orange-500 pb-2 inline-block">Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {['Integrate with your calendar', 'Manage your Notes effectively', 'Task Automation'].map((feature, index) => (
              <div key={index} className="bg-gray-800 p-6 rounded-lg shadow-md transition-all duration-300 hover:shadow-orange-500/50 hover:scale-105 border border-orange-500/20">
                <div className="text-orange-500 text-5xl font-bold mb-4">{index + 1}</div>
                <p className="text-gray-300 text-lg">{feature}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="text-center mb-12 md:mb-16">
          <p className="text-2xl md:text-3xl text-accent font-semibold animate-pulse">
            Stay tuned for updates <span className="inline-block animate-bounce">:)</span>
          </p>
        </section>

        <section className="mb-12 md:mb-16">
          <h2 className="text-3xl md:text-4xl font-semibold mb-8 text-accent border-b-2 border-accent pb-2 inline-block">About NIA</h2>
          <div className="bg-primary p-8 rounded-lg shadow-md border border-accent/20">
            <p className="text-text text-lg leading-relaxed">
              NIA is your cutting-edge AI assistant, designed to seamlessly integrate into your daily life. 
              From managing your schedule to organizing your thoughts and automating routine tasks, 
              NIA is here to enhance your productivity and simplify your digital experience.
            </p>
          </div>
        </section>

        <footer className="text-center">
          <div className="mb-6">
            <Link href={personalGithubUrl} className="inline-block transition-all duration-300 hover:scale-110">
              <Github className="w-10 h-10 text-accent hover:text-accentDark" />
              <span className="sr-only">GitHub</span>
            </Link>
          </div>
          <p className="text-sm text-text/60">
            &copy; 2024 Isha Chaudhari. All rights reserved.
          </p>
        </footer>
      </main>
    </div>
  )
}


import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full border-b bg-white fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <span className="font-bold text-lg">Learning Platform</span>

        <div className="flex gap-4 text-sm">
          <Link href="/login">Login</Link>
          <Link
            href="/register"
            className="bg-indigo-600 text-white px-3 py-1 rounded-md"
          >
            Sign up
          </Link>
        </div>
      </div>
    </nav>
  );
}
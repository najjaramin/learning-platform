import type { InputHTMLAttributes } from "react"

type InputProps = InputHTMLAttributes<HTMLInputElement>

export function Input({ className = "", ...props }: InputProps) {
  return (
    <input
      className={`w-full border rounded-md p-2 text-sm outline-none focus:border-slate-700 focus:ring-2 focus:ring-slate-200 ${className}`}
      {...props}
    />
  )
}
